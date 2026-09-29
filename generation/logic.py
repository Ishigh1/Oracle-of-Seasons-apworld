import cProfile
import io
import pstats
import time
from collections import defaultdict
from pstats import SortKey
from typing import cast

from BaseClasses import CollectionState, EntranceType, Item, Region
from Options import Accessibility
from rule_builder.rules import And, Or, True_

from ..data.Constants import DUNGEON_NAMES, PORTAL_CONNECTIONS, OracleOfSeasonsConnectionType
from ..data.logic import LogicLine
from ..data.logic.dungeons_logic import (
    make_d0_logic,
    make_d1_logic,
    make_d2_logic,
    make_d3_logic,
    make_d4_logic,
    make_d5_logic,
    make_d6_logic,
    make_d7_logic,
    make_d8_logic,
    make_d11_logic,
)
from ..data.logic.logic_predicates import (
    oos_can_jump_1_wide_pit,
    oos_can_jump_5_wide_pit,
    oos_can_kill_magunesu,
    oos_can_kill_normal_enemy,
    oos_can_kill_stalfos,
    oos_has_feather,
    oos_has_flippers,
    oos_has_magnet_gloves,
    oos_has_small_keys,
    oos_option_hard_logic,
    oos_option_medium_logic,
)
from ..data.logic.overworld_logic import make_holodrum_logic
from ..data.logic.rulebuilder import OoSCanReachRegion, Rule
from ..data.logic.subrosia_logic import make_subrosia_logic
from ..world import OracleOfSeasonsWorld


def create_randomizable_connections(
    world: OracleOfSeasonsWorld, prefix: str, vanilla_connections: dict[str, str], outer_group: int, inner_group: int
):
    for reg1, reg2 in vanilla_connections.items():
        region_1 = world.get_region(reg1)
        region_2 = world.get_region(reg2)

        entrance = region_1.create_exit(f"{prefix}{reg1}")
        entrance.randomization_group = outer_group
        entrance.randomization_type = EntranceType.TWO_WAY
        world.set_rule(entrance, True_())

        entrance = region_1.create_er_target(f"{prefix}{reg1}")
        entrance.randomization_group = outer_group
        entrance.randomization_type = EntranceType.TWO_WAY

        entrance = region_2.create_exit(f"{prefix}{reg2}")
        entrance.randomization_group = inner_group
        entrance.randomization_type = EntranceType.TWO_WAY
        world.set_rule(entrance, True_())

        entrance = region_2.create_er_target(f"{prefix}{reg2}")
        entrance.randomization_group = inner_group
        entrance.randomization_type = EntranceType.TWO_WAY


def create_connections(world: OracleOfSeasonsWorld, options):
    profiler = cProfile.Profile()
    profiler.enable()
    all_logic: list[list[LogicLine]] = [
        make_holodrum_logic(world, options),
        make_subrosia_logic(options),
        make_d0_logic(),
        make_d1_logic(),
        make_d2_logic(world, options),
        make_d3_logic(),
        make_d4_logic(options),
        make_d5_logic(),
        make_d6_logic(),
        make_d7_logic(),
        make_d8_logic(),
        make_d11_logic(options),
    ]
    if not world.options.shuffle_dungeons:
        dungeon_entrances: list[LogicLine] = []
        for reg1, reg2 in world.dungeon_entrances.items():
            dungeon_entrances.append((reg1, reg2, True, True_()))
        all_logic.append(dungeon_entrances)

    if not world.options.shuffle_portals:
        portal_connections: list[LogicLine] = []
        for reg1, reg2 in PORTAL_CONNECTIONS.items():
            portal_connections.append((reg1, reg2, True, True_()))
        all_logic.append(portal_connections)

    region_replacement: dict[str, str] = world.region_replacement
    reverse_replacement: dict[str, list[str]] = defaultdict(lambda: [])
    connection_data: dict[tuple[str, str], Rule] = {}
    known_connections: dict[str, list[tuple[str, str]]] = defaultdict(lambda: [])
    needed_regions: set[str] = set()
    for logic_array in all_logic:
        for entrance_desc in logic_array:
            assert len(entrance_desc) == 4

            region_1 = cast(str, entrance_desc[0])
            region_2 = cast(str, entrance_desc[1])
            is_two_way = cast(bool, entrance_desc[2])
            rule = cast(Rule, entrance_desc[3])

            if region_1 in region_replacement:
                region_1 = region_replacement[region_1]
            if region_2 in region_replacement:
                region_2 = region_replacement[region_2]

            if region_1 == region_2:
                continue

            resolved_rule = rule.resolve(world)
            if resolved_rule.always_false:
                continue
            if is_two_way and resolved_rule.always_true:
                # This connection is superfluous
                needed_regions.add(region_1)
                needed_regions.discard(region_2)
                region_replacement[region_2] = region_1
                reverse_replacement[region_1].append(region_2)
                if region_2 in reverse_replacement:
                    to_link_back = reverse_replacement[region_2]
                    for region in to_link_back:
                        region_replacement[region] = region_1
                    reverse_replacement[region_1].extend(to_link_back)

                if region_2 in known_connections:
                    for connection_pair in known_connections.pop(region_2):
                        if connection_pair in connection_data:
                            # That connection may have been severed already
                            (region_a, region_b) = connection_pair
                            rule = connection_data.pop(connection_pair)
                            if region_a == region_2:
                                new_pair = (region_1, region_b)
                            else:
                                new_pair = (region_a, region_1)
                            if new_pair in connection_data:
                                connection_data[new_pair] |= rule
                            else:
                                connection_data[new_pair] = rule
                                known_connections[new_pair[0]].append(new_pair)
                                known_connections[new_pair[1]].append(new_pair)
                pass
            else:
                needed_regions.add(region_1)
                needed_regions.add(region_2)
                connection_pair = (region_1, region_2)
                if connection_pair in connection_data:
                    connection_data[connection_pair] |= rule
                else:
                    connection_data[connection_pair] = rule
                    known_connections[region_1].append(connection_pair)
                    known_connections[region_2].append(connection_pair)
                if is_two_way:
                    connection_pair = (region_2, region_1)
                    if connection_pair in connection_data:
                        connection_data[connection_pair] |= rule
                    else:
                        connection_data[connection_pair] = rule
                        known_connections[region_1].append(connection_pair)
                        known_connections[region_2].append(connection_pair)

    for region in needed_regions:
        world.multiworld.regions.append(Region(region, world.player, world.multiworld))

    for regions, rule in connection_data.items():
        region_1, region_2 = regions
        if region_1 == region_2:
            continue
        region_1 = world.get_region(region_1)
        region_2 = world.get_region(region_2)
        world.create_entrance(region_1, region_2, rule=rule)

    if world.options.shuffle_dungeons:
        create_randomizable_connections(
            world,
            "",
            world.dungeon_entrances,
            OracleOfSeasonsConnectionType.CONNECT_DUNGEON_OVERWORLD,
            OracleOfSeasonsConnectionType.CONNECT_DUNGEON_INSIDE,
        )

    if world.options.shuffle_portals:
        create_randomizable_connections(
            world,
            "enter ",
            PORTAL_CONNECTIONS,
            OracleOfSeasonsConnectionType.CONNECT_PORTAL_OVERWORLD,
            OracleOfSeasonsConnectionType.CONNECT_PORTAL_SUBROSIA,
        )
    profiler.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


class AlwaysAllowRule:
    def __init__(self, world: OracleOfSeasonsWorld, rule: Rule, *item_names: str):
        self.rule = rule.resolve(world)
        self.item_names = item_names
        self.player = world.player

    def __call__(self, state: CollectionState, item: Item):
        return item.player == self.player and item.name in self.item_names and self.rule(state)


def apply_self_locking_rules(world: OracleOfSeasonsWorld):
    if world.options.accessibility == Accessibility.option_full:
        return

    # Process self-locking keys first
    key_rules = {
        "Hero's Cave: Final Chest": AlwaysAllowRule(
            world, OoSCanReachRegion("enter d0"), f"Small Key ({DUNGEON_NAMES[0]})", f"Master Key ({DUNGEON_NAMES[0]})"
        ),
        "Gnarled Root Dungeon: Item in Basement": AlwaysAllowRule(
            world, OoSCanReachRegion("d1 railway chest"), f"Small Key ({DUNGEON_NAMES[1]})"
        ),
        "Poison Moth's Lair (1F): Chest in Mimics Room": AlwaysAllowRule(
            world, And(OoSCanReachRegion("d3 water room"), oos_can_kill_normal_enemy()), f"Small Key ({DUNGEON_NAMES[3]})"
        ),
        "Dancing Dragon Dungeon (1F): Crumbling Room Chest": AlwaysAllowRule(
            world, OoSCanReachRegion("d4 final minecart"), f"Small Key ({DUNGEON_NAMES[4]})"
        ),
        "Dancing Dragon Dungeon (1F): Eye Diving Spot Item": AlwaysAllowRule(
            world, And(OoSCanReachRegion("d4 final minecart"), oos_has_flippers()), f"Small Key ({DUNGEON_NAMES[4]})"
        ),
        "Unicorn's Cave: Magnet Gloves Chest": AlwaysAllowRule(
            world, OoSCanReachRegion("enter d5"), f"Small Key ({DUNGEON_NAMES[5]})"
        ),
        "Unicorn's Cave: Treadmills Basement Item": AlwaysAllowRule(
            world,
            And(
                OoSCanReachRegion("enter d5"),
                oos_has_small_keys(5, 3),
                OoSCanReachRegion("d5 drop ball"),
                oos_has_magnet_gloves(),
                Or(oos_can_kill_magunesu(), And(oos_option_medium_logic(), oos_has_feather())),
            ),
            f"Small Key ({DUNGEON_NAMES[5]})",
        ),
        "Explorer's Crypt (B1F): Chest in Jumping Stalfos Room": AlwaysAllowRule(
            world,
            And(
                OoSCanReachRegion("enter d7"),
                oos_has_small_keys(7, 4),
                Or(oos_can_jump_5_wide_pit(), And(oos_option_hard_logic(), oos_can_jump_1_wide_pit(False))),
                oos_can_kill_stalfos(),
            ),
            f"Small Key ({DUNGEON_NAMES[7]})",
        ),
        "Explorer's Crypt (1F): Chest Right of Entrance": AlwaysAllowRule(
            world,
            And(
                OoSCanReachRegion("enter d7"),
                oos_can_kill_normal_enemy(),
                oos_has_small_keys(7, 1),
            ),
            f"Small Key ({DUNGEON_NAMES[7]})",
        ),
    }

    for location_name, key_rule in key_rules.items():
        location = world.get_location(location_name)
        location.always_allow = key_rule

    # Process other self-locking items
    OTHER_SELF_LOCKING_ITEMS = {
        "North Horon: Malon Trade": "Cuccodex",
        "Maple Trade": "Lon Lon Egg",
        "Holodrum Plain: Mrs. Ruul Trade": "Ghastly Doll",
        "Subrosia: Subrosian Chef Trade": "Iron Pot",
        "Sunken City: Ingo Trade": "Goron Vase",
        "North Horon: Yelling Old Man Trade": "Fish",
        "Horon Village: Tick Tock Trade": "Wooden Bird",
        "Eastern Suburbs: Guru-Guru Trade": "Engine Grease",
        "Subrosia: Smithy Hard Ore Reforge": "Hard Ore",
        "Subrosia: Smithy Rusty Bell Reforge": "Rusty Bell",
        "Sunken City: Master's Plaque Trade": "Master's Plaque",
        "Subrosia: Market #1": "Star Ore",
    }
    if not world.options.secret_locations:
        OTHER_SELF_LOCKING_ITEMS["Goron Mountain: Biggoron Trade"] = "Lava Soup"

    for loc_name, item_name in OTHER_SELF_LOCKING_ITEMS.items():
        location = world.get_location(loc_name)
        region = cast(Region, location.parent_region)
        parent_region = cast(Region, region.entrances[0].parent_region)
        location.always_allow = AlwaysAllowRule(world, OoSCanReachRegion(parent_region.name), item_name)

    # Great Furnace special case
    location = world.get_location("Subrosia: Item Smelted in Great Furnace")
    location.always_allow = AlwaysAllowRule(world, OoSCanReachRegion("great furnace"), "Red Ore", "Blue Ore")


def apply_rule_forbiddance(world: OracleOfSeasonsWorld):
    rupee_shops = [
        "Horon Village: Shop #1",
        "Horon Village: Shop #2",
        "Horon Village: Shop #3",
        "Horon Village: Member's Shop #1",
        "Horon Village: Member's Shop #2",
        "Horon Village: Member's Shop #3",
        "Sunken City: Syrup Shop #1",
        "Sunken City: Syrup Shop #2",
        "Sunken City: Syrup Shop #3",
    ]
    if world.options.advance_shop:
        rupee_shops.extend(
            [
                "Horon Village: Advance Shop #1",
                "Horon Village: Advance Shop #2",
                "Horon Village: Advance Shop #3",
            ]
        )

    def rupee_rule(item: Item):
        return item.player != world.player or not item.code or ((item.code & 0xFF00) != 0x2800)  # 28 being rupees

    for rupee_shop in rupee_shops:
        location = world.get_location(rupee_shop)
        location.item_rule = rupee_rule

    def ore_rule(item: Item):
        return item.player != world.player or not item.code or ((item.code & 0xFF00) != 0x3700)  # 37 being ores

    for ore_shop in ["Subrosia: Market #2", "Subrosia: Market #3", "Subrosia: Market #4", "Subrosia: Market #5"]:
        location = world.get_location(ore_shop)
        location.item_rule = ore_rule
