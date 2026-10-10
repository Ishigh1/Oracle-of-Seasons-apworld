from rule_builder.rules import And, CanReachRegion, Has, Or, True_

from ... import OracleOfSeasonsWorld
from ...options import (
    OracleOfSeasonsIncludeSecretLocations,
    OracleOfSeasonsLogicDifficulty,
    OracleOfSeasonsOptions,
    OracleOfSeasonsRemoveD0AltEntrance,
    OracleOfSeasonsRemoveD2AltEntrance,
    OracleOfSeasonsTarmGateRequirement,
)
from ..Constants import SEASON_AUTUMN, SEASON_SPRING, SEASON_SUMMER, SEASON_WINTER
from ..regions import GASHA_REGIONS, RegionName
from . import LogicLine
from .logic_predicates import (
    oos_can_beat_required_golden_beasts,
    oos_can_break_bush,
    oos_can_break_flowers,
    oos_can_break_mushroom,
    oos_can_complete_lost_woods_main_sequence,
    oos_can_dimitri_clip,
    oos_can_farm_rupees,
    oos_can_harvest_gasha,
    oos_can_harvest_tree,
    oos_can_jump_1_wide_liquid,
    oos_can_jump_1_wide_pit,
    oos_can_jump_2_wide_liquid,
    oos_can_jump_2_wide_pit,
    oos_can_jump_3_wide_liquid,
    oos_can_jump_3_wide_pit,
    oos_can_jump_4_wide_liquid,
    oos_can_jump_4_wide_pit,
    oos_can_jump_5_wide_liquid,
    oos_can_jump_5_wide_pit,
    oos_can_jump_6_wide_pit,
    oos_can_kill_armored_enemy,
    oos_can_kill_facade,
    oos_can_kill_moldorm,
    oos_can_meet_maple,
    oos_can_reach_lost_woods_pedestal,
    oos_can_reach_rooster_adventure,
    oos_can_remove_rockslide,
    oos_can_remove_season,
    oos_can_remove_snow,
    oos_can_summon_dimitri,
    oos_can_summon_moosh,
    oos_can_summon_ricky,
    oos_can_swim,
    oos_can_trigger_lever,
    oos_can_use_ember_seeds,
    oos_can_use_mystery_seeds,
    oos_can_use_pegasus_seeds,
    oos_can_use_seeds,
    oos_has_autumn,
    oos_has_biggoron_sword,
    oos_has_bombchus,
    oos_has_bombchus_for_bombjump,
    oos_has_bombchus_for_tiles,
    oos_has_bombs,
    oos_has_bombs_for_bombjump,
    oos_has_bombs_for_tiles,
    oos_has_bracelet,
    oos_has_cane,
    oos_has_cape,
    oos_has_ember_seeds,
    oos_has_essences,
    oos_has_essences_for_maku_seed,
    oos_has_essences_for_treehouse,
    oos_has_feather,
    oos_has_flippers,
    oos_has_flute,
    oos_has_fools_ore,
    oos_has_gale_seeds,
    oos_has_hearts_by_difficulty,
    oos_has_magic_boomerang,
    oos_has_magnet_gloves,
    oos_has_mystery_seeds,
    oos_has_noble_sword,
    oos_has_pegasus_seeds,
    oos_has_prog,
    oos_has_required_jewels,
    oos_has_rod,
    oos_has_rupees_for_shop,
    oos_has_satchel,
    oos_has_scent_seeds,
    oos_has_season,
    oos_has_seed_thrower,
    oos_has_shield,
    oos_has_shovel,
    oos_has_spring,
    oos_has_summer,
    oos_has_switch_hook,
    oos_has_sword,
    oos_has_tight_switch_hook,
    oos_has_winter,
    oos_is_companion_moosh,
    oos_is_companion_ricky,
    oos_is_default_season,
    oos_not_season_in_eastern_suburbs,
    oos_option_hard_logic,
    oos_option_hell_logic,
    oos_option_medium_logic,
    oos_roosters,
    oos_season_in_central_woods_of_winter,
    oos_season_in_eastern_suburbs,
    oos_season_in_eyeglass_lake,
    oos_season_in_holodrum_plain,
    oos_season_in_horon_village,
    oos_season_in_lost_woods,
    oos_season_in_mt_cucco,
    oos_season_in_spool_swamp,
    oos_season_in_sunken_city,
    oos_season_in_tarm_ruins,
    oos_season_in_temple_remains,
    oos_season_in_western_coast,
    oos_season_in_woods_of_winter,
    oos_self_locking_item,
)
from .rulebuilder import from_option


def make_holodrum_logic(world: OracleOfSeasonsWorld, options: OracleOfSeasonsOptions) -> list[LogicLine]:
    return [
        (
            RegionName.maple_encounter,
            RegionName.maple_trade,
            False,
            Or(Has("Lon Lon Egg"), oos_self_locking_item("Maple Trade", "Lon Lon Egg")),
        ),
        (RegionName.maple_encounter, RegionName.maple_rare_item_1, False, oos_has_prog(15)),
        (RegionName.maple_rare_item_1, RegionName.maple_rare_item_2, False, oos_has_prog(30)),
        (RegionName.maple_rare_item_2, RegionName.maple_rare_item_3, False, oos_has_prog(45)),
        (RegionName.maple_rare_item_3, RegionName.maple_rare_item_4, False, oos_has_prog(60)),
        (RegionName.horon_village, RegionName.mayors_gift, False, True_()),
        (RegionName.horon_village, RegionName.vasus_gift, False, True_()),
        (RegionName.horon_village, RegionName.mayors_house_secret_room, False, oos_can_remove_rockslide(False)),
        (
            RegionName.horon_village,
            RegionName.horon_heart_piece,
            False,
            Or(oos_can_use_ember_seeds(False), oos_can_dimitri_clip()),
        ),
        (RegionName.horon_village, RegionName.dr_left_reward, False, oos_can_use_ember_seeds(True)),
        (RegionName.horon_village, RegionName.old_man_in_horon, False, oos_can_use_ember_seeds(False)),
        (
            RegionName.horon_village,
            RegionName.old_man_trade,
            False,
            Or(Has("Fish"), oos_self_locking_item("North Horon: Yelling Old Man Trade", "Fish")),
        ),
        (
            RegionName.horon_village,
            RegionName.tick_tock_trade,
            False,
            Or(Has("Wooden Bird"), oos_self_locking_item("Horon Village: Tick Tock Trade", "Wooden Bird")),
        ),
        (RegionName.horon_village, RegionName.maku_tree, False, oos_has_sword(False)),
        (
            RegionName.horon_village,
            RegionName.horon_village_SE_chest,
            False,
            And(
                oos_can_remove_rockslide(False),
                Or(
                    oos_can_swim(False),
                    oos_season_in_horon_village(SEASON_WINTER),
                    oos_can_jump_2_wide_liquid(allow_bombchus=True),
                ),
            ),
        ),
        (
            RegionName.horon_village,
            RegionName.horon_village_SW_chest,
            False,
            Or(And(oos_season_in_horon_village(SEASON_AUTUMN), oos_can_break_mushroom(True)), oos_can_dimitri_clip()),
        ),
        (
            RegionName.horon_village,
            RegionName.horon_village_portal,
            False,
            Or(oos_has_magic_boomerang(), oos_can_jump_6_wide_pit()),
        ),
        (
            RegionName.horon_village_portal,
            RegionName.horon_village,
            False,
            Or(oos_can_trigger_lever(), oos_can_jump_6_wide_pit()),
        ),
        (RegionName.horon_village, RegionName.horon_village_tree, False, oos_can_harvest_tree(True)),
        (RegionName.horon_village, RegionName.horon_shop, False, oos_has_rupees_for_shop("horonShop")),
        (
            RegionName.horon_village,
            RegionName.advance_shop,
            False,
            oos_has_rupees_for_shop("advanceShop"),
            bool(options.advance_shop),
        ),
        (
            RegionName.horon_village,
            RegionName.members_shop,
            False,
            And(Has("Member's Card"), oos_has_rupees_for_shop("memberShop")),
        ),
        (
            RegionName.horon_village,
            RegionName.clock_shop_secret,
            False,
            And(
                oos_has_shovel(),
                Or(
                    oos_has_noble_sword(),
                    oos_has_biggoron_sword(),
                    oos_has_fools_ore(),
                    And(oos_option_medium_logic(), Or(oos_has_sword(), oos_has_bombchus(3))),
                ),
            ),
            bool(options.secret_locations),
        ),
        # WESTERN COAST ##############################################################################################
        (RegionName.horon_village, RegionName.western_coast, True, True_()),
        (RegionName.western_coast, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.western_coast,
            RegionName.black_beasts_chest,
            False,
            And(
                And(
                    oos_has_seed_thrower(),
                    oos_can_use_ember_seeds(True),
                ),
                oos_can_use_mystery_seeds(),
                oos_can_kill_moldorm(),
            ),
        ),
        (RegionName.western_coast, RegionName.d0_entrance, True, True_()),
        (
            RegionName.western_coast,
            RegionName.d0_rupee_chest,
            False,
            And(
                from_option(OracleOfSeasonsRemoveD0AltEntrance, OracleOfSeasonsRemoveD0AltEntrance.option_false),
                oos_can_break_bush(True),
            ),
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.western_coast,
            False,
            And(Has("_met_pirates"), Has("Pirate's Bell")),
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.coast_stump,
            False,
            And(oos_can_remove_rockslide(False), Or(oos_has_feather(), oos_option_hard_logic())),
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.old_man_near_western_coast_house,
            False,
            oos_can_use_ember_seeds(False),
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.d7_entrance,
            False,
            And(
                Or(oos_can_jump_3_wide_pit(), oos_season_in_western_coast(SEASON_SUMMER)),
                Or(
                    oos_has_shovel(),
                    oos_is_default_season("WESTERN_COAST", SEASON_WINTER, False),
                    And(CanReachRegion(RegionName.coast_stump), oos_can_remove_season(SEASON_WINTER)),
                ),
            ),
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.graveyard_heart_piece,
            False,
            And(oos_season_in_western_coast(SEASON_AUTUMN), oos_can_jump_3_wide_pit(), oos_can_break_mushroom(False)),
        ),
        (
            RegionName.d7_entrance,
            RegionName.graveyard_heart_piece,
            False,
            And(oos_is_default_season("WESTERN_COAST", SEASON_AUTUMN), oos_can_break_mushroom(False)),
        ),
        (RegionName.d7_entrance, RegionName.graveyard_secret, False, oos_has_shovel(), bool(options.secret_locations)),
        (
            RegionName.d7_entrance,
            RegionName.western_coast_after_ship,
            False,
            Or(
                oos_is_default_season("WESTERN_COAST", SEASON_WINTER, False),
                oos_has_shovel(),
            ),
        ),
        # EASTERN SUBURBS #############################################################################################
        (RegionName.horon_village, RegionName.suburbs, True, oos_can_use_ember_seeds(False)),
        (RegionName.suburbs, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.suburbs,
            RegionName.windmill_heart_piece,
            False,
            Or(oos_season_in_eastern_suburbs(SEASON_WINTER), oos_can_dimitri_clip()),
        ),
        (
            RegionName.suburbs,
            RegionName.guru_guru_trade,
            False,
            Or(Has("Engine Grease"), oos_self_locking_item("Eastern Suburbs: Guru-Guru Trade", "Engine Grease")),
        ),
        (
            RegionName.suburbs,
            RegionName.eastern_suburbs_spring_cave,
            False,
            And(
                oos_has_bracelet(),
                oos_season_in_eastern_suburbs(SEASON_SPRING),
                Or(oos_has_magnet_gloves(), oos_can_jump_3_wide_pit()),
            ),
        ),
        (RegionName.eastern_suburbs_portal, RegionName.suburbs, False, oos_can_break_bush(False)),
        (RegionName.suburbs, RegionName.eastern_suburbs_portal, False, oos_can_break_bush(True)),
        (
            RegionName.suburbs,
            RegionName.suburbs_fairy_fountain,
            True,
            And(
                Or(oos_can_swim(True), oos_can_jump_1_wide_liquid(True), oos_has_switch_hook()),
                oos_not_season_in_eastern_suburbs(SEASON_WINTER),
            ),
        ),
        (RegionName.suburbs_fairy_fountain, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.suburbs_fairy_fountain, RegionName.suburbs_fairy_fountain_winter, False, oos_has_winter()),
        # Should be a useless transition, but it might be useful someday
        (
            RegionName.suburbs,
            RegionName.suburbs_fairy_fountain_winter,
            True,
            oos_season_in_eastern_suburbs(SEASON_WINTER),
        ),
        (RegionName.suburbs_fairy_fountain_winter, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.suburbs_fairy_fountain_winter,
            RegionName.suburbs_fairy_fountain,
            False,
            oos_can_remove_season(SEASON_WINTER),
        ),
        (
            RegionName.suburbs_fairy_fountain,
            RegionName.sunken_city_entrance,
            False,
            oos_season_in_eastern_suburbs(SEASON_SPRING),
        ),
        (
            RegionName.sunken_city_entrance,
            RegionName.suburbs_fairy_fountain,
            False,
            oos_not_season_in_eastern_suburbs(SEASON_WINTER),
        ),
        (
            RegionName.sunken_city_entrance,
            RegionName.suburbs_fairy_fountain_winter,
            False,
            oos_season_in_eastern_suburbs(SEASON_WINTER),
        ),
        # WOODS OF WINTER / 2D SECTOR ################################################################################
        (RegionName.suburbs_fairy_fountain_winter, RegionName.moblin_road, False, True_()),
        (
            RegionName.moblin_road,
            RegionName.suburbs_fairy_fountain_winter,
            False,
            oos_season_in_eastern_suburbs(SEASON_WINTER),
        ),
        (RegionName.moblin_road, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.sunken_city_entrance,
            RegionName.moblin_road,
            False,
            And(
                oos_has_flippers(),
                Or(oos_is_default_season("SUNKEN_CITY", SEASON_WINTER, False), oos_can_remove_season(SEASON_WINTER)),
            ),
        ),
        (
            RegionName.moblin_road,
            RegionName.woods_of_winter_1st_cave,
            False,
            And(
                oos_can_remove_rockslide(True),
                oos_can_break_bush(False, True),
                Or(
                    oos_is_default_season("WOODS_OF_WINTER", SEASON_WINTER, False), oos_can_remove_season(SEASON_WINTER)
                ),
            ),
        ),
        (
            RegionName.moblin_road,
            RegionName.woods_of_winter_2nd_cave,
            False,
            Or(oos_can_swim(False), oos_can_jump_3_wide_liquid(allow_bombchus=True)),
        ),
        (RegionName.moblin_road, RegionName.hollys_house, False, oos_season_in_woods_of_winter(SEASON_WINTER)),
        (RegionName.moblin_road, RegionName.old_man_near_hollys_house, False, oos_can_use_ember_seeds(False)),
        (
            RegionName.moblin_road,
            RegionName.woods_of_winter_heart_piece,
            False,
            Or(oos_can_swim(True), oos_has_bracelet(), oos_can_jump_1_wide_liquid(True)),
        ),
        (RegionName.suburbs_fairy_fountain, RegionName.central_woods_of_winter, False, True_()),
        (
            RegionName.suburbs_fairy_fountain_winter,
            RegionName.central_woods_of_winter,
            False,
            Or(
                And(oos_can_jump_1_wide_pit(True), oos_has_bracelet()),
                And(oos_option_medium_logic(), oos_has_switch_hook(), oos_has_bracelet()),
                oos_can_remove_snow(True),
            ),
        ),
        (
            RegionName.central_woods_of_winter,
            RegionName.suburbs_fairy_fountain,
            False,
            oos_is_default_season("EASTERN_SUBURBS", SEASON_WINTER, False),
        ),
        (
            RegionName.central_woods_of_winter,
            RegionName.suburbs_fairy_fountain_winter,
            False,
            And(
                oos_is_default_season("EASTERN_SUBURBS", SEASON_WINTER),
                Or(
                    And(oos_can_jump_1_wide_pit(True), oos_has_bracelet()),
                    And(oos_option_medium_logic(), oos_has_switch_hook(), oos_has_bracelet()),
                    oos_can_remove_snow(True),
                ),
            ),
        ),
        (RegionName.central_woods_of_winter, RegionName.woods_of_winter_tree, False, oos_can_harvest_tree(True)),
        (RegionName.central_woods_of_winter, RegionName.d2_entrance, True, oos_can_break_bush(True, True)),
        (
            RegionName.central_woods_of_winter,
            RegionName.cave_outside_D2,
            False,
            And(
                Or(
                    And(
                        oos_season_in_central_woods_of_winter(SEASON_AUTUMN),
                        oos_can_break_mushroom(True),
                    ),
                    oos_can_dimitri_clip(),
                ),
                Or(oos_can_jump_4_wide_pit(), oos_has_magnet_gloves()),
            ),
        ),
        (RegionName.central_woods_of_winter, RegionName.d2_stump, True, True_()),
        (RegionName.d2_stump, RegionName.d2_roof, True, oos_has_bracelet()),
        (
            RegionName.d2_roof,
            RegionName.d2_alt_entrances,
            # Do not allow for turning back if the dungeon is excluded
            not options.exclude_dungeons_without_essence.value or "Gift of Time" in world.essences_in_game,
            from_option(OracleOfSeasonsRemoveD2AltEntrance, OracleOfSeasonsRemoveD2AltEntrance.option_false),
        ),
        (RegionName.central_woods_of_winter, RegionName.mystery_owl, False, oos_can_use_mystery_seeds()),
        # EYEGLASS LAKE SECTOR #########################################################################################
        (RegionName.impas_house, RegionName.horon_village, True, True_()),
        (RegionName.impas_house, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.impas_house,
            RegionName.eyeglass_lake_across_bridge,
            False,
            Or(
                oos_can_jump_4_wide_pit(),
                And(
                    oos_has_feather(),
                    Or(
                        oos_is_default_season("EYEGLASS_LAKE", SEASON_AUTUMN),
                        And(oos_has_autumn(), oos_can_break_bush(True)),
                    ),
                ),
            ),
        ),
        (RegionName.impas_house, RegionName.d1_stump, True, oos_can_break_bush(True, True)),
        (RegionName.d1_stump, RegionName.north_horon, True, oos_has_bracelet()),
        (
            RegionName.d1_stump,
            RegionName.malon_trade,
            False,
            Or(Has("Cuccodex"), oos_self_locking_item("North Horon: Malon Trade", "Cuccodex")),
        ),
        (RegionName.d1_stump, RegionName.d1_island, True, oos_can_break_bush(True, True)),
        (RegionName.d1_stump, RegionName.old_man_near_d1, False, oos_can_use_ember_seeds(False)),
        (RegionName.d1_island, RegionName.d1_entrance, True, Has("Gnarled Key")),
        (
            RegionName.d1_island,
            RegionName.golden_beasts_old_man,
            False,
            And(
                Or(
                    oos_is_default_season("EYEGLASS_LAKE", SEASON_SUMMER),
                    And(oos_has_summer(), oos_can_break_bush(True)),
                ),
                oos_can_beat_required_golden_beasts(),
            ),
        ),
        (
            RegionName.d1_stump,
            RegionName.eyeglass_lake_default,
            True,
            And(
                Or(
                    oos_season_in_eyeglass_lake(SEASON_SPRING),
                    oos_season_in_eyeglass_lake(SEASON_AUTUMN),
                ),
                oos_can_jump_1_wide_pit(True),
                Or(
                    oos_can_swim(False),
                    And(
                        # To be able to use Dimitri, we need the bracelet to throw him above the pit
                        oos_option_medium_logic(),
                        oos_can_summon_dimitri(),
                        oos_has_bracelet(),
                    ),
                ),
            ),
        ),
        (
            RegionName.d1_stump,
            RegionName.eyeglass_lake_dry,
            True,
            And(oos_season_in_eyeglass_lake(SEASON_SUMMER), oos_can_jump_1_wide_pit(True)),
        ),
        (
            RegionName.d1_stump,
            RegionName.eyeglass_lake_frozen,
            True,
            And(oos_season_in_eyeglass_lake(SEASON_WINTER), oos_can_jump_1_wide_pit(True)),
        ),
        (RegionName.d5_stump, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.d5_stump,
            RegionName.eyeglass_lake_default,
            True,
            And(
                Or(
                    oos_season_in_eyeglass_lake(SEASON_SPRING),
                    oos_season_in_eyeglass_lake(SEASON_AUTUMN),
                ),
                oos_can_swim(True),
            ),
        ),
        (
            RegionName.d5_stump,
            RegionName.eyeglass_lake_dry,
            False,
            And(oos_season_in_eyeglass_lake(SEASON_SUMMER), oos_can_swim(False)),
        ),
        (RegionName.d5_stump, RegionName.eyeglass_lake_frozen, True, oos_season_in_eyeglass_lake(SEASON_WINTER)),
        (
            RegionName.eyeglass_lake_portal,
            RegionName.eyeglass_lake_default,
            False,
            And(
                Or(
                    oos_is_default_season("EYEGLASS_LAKE", SEASON_AUTUMN),
                    oos_is_default_season("EYEGLASS_LAKE", SEASON_SPRING),
                ),
                oos_can_swim(False),
            ),
        ),
        (RegionName.eyeglass_lake_default, RegionName.eyeglass_lake_portal, False, True_()),
        (
            RegionName.eyeglass_lake_portal,
            RegionName.eyeglass_lake_frozen,
            False,
            And(
                oos_is_default_season("EYEGLASS_LAKE", SEASON_WINTER),
                Or(oos_can_swim(False), oos_can_jump_5_wide_liquid()),
            ),
        ),
        (
            RegionName.eyeglass_lake_frozen,
            RegionName.eyeglass_lake_portal,
            False,
            Or(oos_can_swim(True), oos_can_jump_5_wide_liquid()),
        ),
        # This transition has been removed since the anti-softlock has been removed
        # [RegionName.eyeglass_lake_portal, RegionName.eyeglass_lake_dry, False,  \
        #     oos_is_default_season( "EYEGLASS_LAKE", SEASON_SUMMER)),
        # Instead, jump straight from the portal to lost woods in summer
        (
            RegionName.eyeglass_lake_portal,
            RegionName.lost_woods,
            False,
            And(oos_option_hard_logic(), oos_is_default_season("EYEGLASS_LAKE", SEASON_SUMMER)),
        ),
        (
            RegionName.eyeglass_lake_dry,
            RegionName.dry_eyeglass_lake_west_cave,
            False,
            And(
                oos_can_remove_rockslide(True),
                oos_can_swim(False),  # chest is surrounded by water
            ),
        ),
        (
            RegionName.d5_stump,
            RegionName.d5_entrance,
            False,
            And(
                # If we don't have autumn, we need to ensure we were able to reach that node with autumn as default
                # season without changing to another season which we wouldn't be able to revert back.
                # For this reason, "default season is autumn" case is handled through direct routes from the lake portal
                # and from D1 stump.
                oos_has_autumn(),
                oos_can_break_mushroom(True),
            ),
        ),
        # Direct route #1 to reach D5 entrance taking advantage of autumn as default season
        (
            RegionName.d1_stump,
            RegionName.d5_entrance,
            False,
            And(
                oos_is_default_season("EYEGLASS_LAKE", SEASON_AUTUMN),
                oos_can_jump_1_wide_pit(True),
                oos_can_break_mushroom(True),
                Or(
                    oos_can_swim(False),
                    And(
                        # To be able to use Dimitri, we need the bracelet to throw him above the pit
                        oos_option_medium_logic(),
                        oos_can_summon_dimitri(),
                        oos_has_bracelet(),
                    ),
                    And(
                        # Alternatively, we can use winter to summon Dimitri then reset the season with the portal
                        oos_can_summon_dimitri(),
                        oos_has_winter(),
                    ),
                ),
            ),
        ),
        # Direct route #2 to reach D5 entrance taking advantage of autumn as default season
        (
            RegionName.eyeglass_lake_portal,
            RegionName.d5_entrance,
            False,
            And(
                oos_is_default_season("EYEGLASS_LAKE", SEASON_AUTUMN), oos_can_swim(False), oos_can_break_mushroom(True)
            ),
        ),
        (
            RegionName.d5_entrance,
            RegionName.d5_stump,
            False,
            Or(
                oos_can_jump_1_wide_pit(True),
                And(
                    oos_is_default_season("EYEGLASS_LAKE", SEASON_AUTUMN),
                    oos_can_break_mushroom(False),
                    # TODO: Maybe change that by removing the anti-softlock
                    #  mechanism that also adds an anti-ricky protection
                    # Alternatively, move the rock up to prevent ricky from jumping while preserving the anti-softlock
                ),
            ),
        ),
        (
            RegionName.d5_stump,
            RegionName.dry_eyeglass_lake_east_cave,
            False,
            And(
                oos_has_summer(),
                oos_has_bracelet(),
            ),
        ),
        (
            RegionName.d5_entrance,
            RegionName.dry_eyeglass_lake_east_cave,
            False,
            And(
                oos_can_jump_1_wide_pit(True),
                oos_is_default_season("EYEGLASS_LAKE", SEASON_SUMMER),
                oos_has_bracelet(),
            ),
        ),
        # NORTH HORON / HOLODRUM PLAIN ###############################################################################
        (RegionName.north_horon, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.north_horon, RegionName.north_horon_tree, False, oos_can_harvest_tree(True)),
        (RegionName.north_horon, RegionName.blaino_prize, False, oos_can_farm_rupees()),
        (
            RegionName.north_horon,
            RegionName.cave_north_of_D1,
            False,
            And(
                Or(
                    And(
                        oos_season_in_holodrum_plain(SEASON_AUTUMN),
                        oos_can_break_mushroom(True),
                    ),
                    oos_can_dimitri_clip(),
                ),
                oos_has_flippers(),
            ),
        ),
        (
            RegionName.north_horon,
            RegionName.old_man_near_blaino,
            False,
            And(
                oos_can_use_ember_seeds(False),
                Or(
                    oos_is_default_season("HOLODRUM_PLAIN", SEASON_SUMMER),
                    oos_can_summon_ricky(),
                    And(
                        # can get from the stump to old man in summer
                        oos_has_summer(),
                        Or(oos_can_jump_1_wide_pit(True), And(oos_can_break_bush(True), oos_can_swim(True))),
                    ),
                ),
            ),
        ),
        (RegionName.north_horon, RegionName.underwater_item_below_natzu_bridge, False, oos_can_swim(False)),
        (RegionName.north_horon, RegionName.temple_remains_lower_stump, False, oos_can_jump_3_wide_pit()),
        (RegionName.north_horon, RegionName.spool_swamp_north, False, Has("Ricky's Gloves")),
        (
            RegionName.temple_remains_lower_stump,
            RegionName.north_horon,
            False,
            Or(oos_can_jump_3_wide_pit(), oos_has_switch_hook()),
        ),
        (RegionName.ghastly_stump, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.ghastly_stump,
            RegionName.mrs_ruul_trade,
            False,
            Or(Has("Ghastly Doll"), oos_self_locking_item("Holodrum Plain: Mrs. Ruul Trade", "Ghastly Doll")),
        ),
        (RegionName.ghastly_stump, RegionName.old_man_near_mrs_ruul, False, oos_can_use_ember_seeds(False)),
        (
            RegionName.north_horon,
            RegionName.ghastly_stump,
            True,
            Or(oos_can_jump_1_wide_pit(True), oos_season_in_holodrum_plain(SEASON_WINTER)),
        ),
        (RegionName.spool_swamp_north, RegionName.ghastly_stump, False, True_()),
        (
            RegionName.ghastly_stump,
            RegionName.spool_swamp_north,
            False,
            Or(
                oos_season_in_holodrum_plain(SEASON_SUMMER),
                oos_can_jump_4_wide_pit(),
                oos_can_summon_ricky(),
                oos_can_summon_moosh(),
            ),
        ),
        (
            RegionName.ghastly_stump,
            RegionName.spool_swamp_south,
            True,
            And(
                oos_can_swim(True),
                oos_can_break_bush(True),
            ),
        ),
        # Goron Mountain <-> North Horon <-> D1 island <-> Spool swamp waterway
        (RegionName.d1_island, RegionName.spool_swamp_south, False, oos_can_swim(True)),
        (
            RegionName.spool_swamp_south_spring,
            RegionName.d1_island,
            False,
            Or(oos_can_summon_dimitri(), And(Has("Swimmer's Ring"), oos_can_swim(False), oos_option_medium_logic())),
        ),
        (RegionName.spool_swamp_south_summer, RegionName.d1_island, False, oos_can_swim(True)),
        (RegionName.spool_swamp_south_autumn, RegionName.d1_island, False, oos_can_swim(True)),
        (RegionName.spool_swamp_south_winter, RegionName.d1_island, False, oos_can_swim(True)),
        (RegionName.d1_island, RegionName.north_horon, True, oos_can_swim(True)),
        (RegionName.north_horon, RegionName.goron_mountain_entrance, True, oos_can_swim(True)),
        (RegionName.goron_mountain_entrance, RegionName.natzu_region_across_water, True, oos_can_swim(True)),
        (
            RegionName.ghastly_stump,
            RegionName.d1_island,
            True,
            And(
                # Technically, Ricky and Moosh don't work to go from the ghastly stump bank to the stump,
                # but both can go through north horon and jump the holes
                oos_can_break_bush(True),
                oos_can_swim(True),
            ),
        ),
        (
            RegionName.d1_island,
            RegionName.old_man_in_treehouse,
            False,
            And(oos_can_swim(True), oos_has_essences_for_treehouse()),
        ),
        (RegionName.d1_island, RegionName.cave_south_of_mrs_ruul, False, oos_can_swim(False)),
        # SPOOL SWAMP #############################################################################################
        (RegionName.spool_swamp_north, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.spool_swamp_north, RegionName.spool_swamp_tree, False, oos_can_harvest_tree(True)),
        (
            RegionName.spool_swamp_north,
            RegionName.floodgate_keepers_house,
            False,
            Or(oos_can_trigger_lever(), And(oos_option_hard_logic(), oos_has_bracelet())),
        ),
        (
            RegionName.spool_swamp_north,
            RegionName.spool_swamp_digging_spot,
            False,
            And(oos_season_in_spool_swamp(SEASON_SUMMER), oos_has_shovel()),
        ),
        (RegionName.floodgate_keepers_house, RegionName.floodgate_owl, False, oos_can_use_mystery_seeds()),
        (
            RegionName.floodgate_keepers_house,
            RegionName.floodgate_keyhole,
            False,
            And(
                Or(
                    oos_can_use_pegasus_seeds(),
                    oos_has_cape(),
                    oos_has_flippers(),
                    And(
                        # The cane doesn't hold the button
                        oos_option_medium_logic(),
                        oos_has_cane(),
                    ),
                    And(
                        oos_option_medium_logic(),
                        oos_has_feather(),
                    ),
                ),
                oos_has_bracelet(),
            ),
        ),
        (
            RegionName.floodgate_keyhole,
            RegionName.spool_swamp_scrub,
            False,
            oos_has_rupees_for_shop("spoolSwampScrub"),
            bool(options.shuffle_business_scrubs),
        ),
        (RegionName.floodgate_keyhole, RegionName.spool_stump, False, Has("Floodgate Key")),
        (RegionName.spool_stump, RegionName.d3_entrance, False, oos_season_in_spool_swamp(SEASON_SUMMER)),
        (
            RegionName.d3_entrance,
            RegionName.spool_swamp_north,
            False,
            # Coming from alt d0/d2
            oos_can_swim(False),
        ),
        (
            RegionName.spool_stump,
            RegionName.spool_swamp_middle,
            False,
            Or(
                oos_is_default_season("SPOOL_SWAMP", SEASON_SPRING, False),
                oos_can_remove_season(SEASON_SPRING),
                oos_can_swim(True),
            ),
        ),
        (RegionName.spool_swamp_middle, RegionName.spool_swamp_south_near_gasha_spot, False, oos_can_summon_ricky()),
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_middle,
            False,
            Or(
                oos_can_summon_ricky(),
                And(
                    oos_has_feather(),
                    Or(
                        oos_has_magic_boomerang(),
                        And(
                            oos_option_medium_logic(),
                            Or(
                                oos_has_sword(),
                                And(
                                    oos_has_seed_thrower(),
                                    oos_can_use_ember_seeds(False),
                                ),
                                And(oos_has_bombs_for_tiles(), oos_option_hard_logic()),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        (RegionName.spool_swamp_south_near_gasha_spot, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.spool_swamp_south_near_gasha_spot, RegionName.spool_swamp_portal, True, oos_has_bracelet()),
        (
            RegionName.spool_swamp_middle,
            RegionName.spool_swamp_south,
            True,
            Or(oos_can_jump_2_wide_pit(), oos_can_summon_moosh(), oos_can_swim(True)),
        ),
        (RegionName.spool_swamp_south, RegionName.maple_encounter, False, oos_can_meet_maple()),
        # make sure you can go directly from the stump to south, or default season
        # just because you can reach the stump doesn't mean you can also get there
        # ex. only access to gasha section is through subrosia
        (
            RegionName.spool_swamp_south,
            RegionName.spool_swamp_south_spring,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_SPRING),
        ),
        (
            RegionName.spool_stump,
            RegionName.spool_swamp_south_spring,
            False,
            And(
                oos_has_spring(),
                oos_can_swim(True),
                Or(oos_can_summon_ricky(), oos_can_summon_moosh(), oos_can_jump_2_wide_pit()),
            ),
        ),
        (
            RegionName.spool_swamp_south,
            RegionName.spool_swamp_south_summer,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_SUMMER),
        ),
        (
            RegionName.spool_stump,
            RegionName.spool_swamp_south_summer,
            False,
            And(
                oos_has_summer(),
                Or(oos_can_swim(True), oos_can_summon_ricky(), oos_can_summon_moosh(), oos_can_jump_2_wide_pit()),
            ),
        ),
        (
            RegionName.spool_swamp_south,
            RegionName.spool_swamp_south_autumn,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_AUTUMN),
        ),
        (
            RegionName.spool_stump,
            RegionName.spool_swamp_south_autumn,
            False,
            And(
                oos_has_autumn(),
                Or(oos_can_swim(True), oos_can_summon_ricky(), oos_can_summon_moosh(), oos_can_jump_2_wide_pit()),
            ),
        ),
        (
            RegionName.spool_swamp_south,
            RegionName.spool_swamp_south_winter,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_WINTER),
        ),
        (
            RegionName.spool_stump,
            RegionName.spool_swamp_south_winter,
            False,
            And(
                oos_has_winter(),
                Or(oos_can_swim(True), oos_can_summon_ricky(), oos_can_summon_moosh(), oos_can_jump_2_wide_pit()),
            ),
        ),
        (RegionName.spool_swamp_south_winter, RegionName.spool_swamp_south, False, True_()),
        (RegionName.spool_swamp_south_spring, RegionName.spool_swamp_south, False, True_()),
        (RegionName.spool_swamp_south_summer, RegionName.spool_swamp_south, False, True_()),
        (RegionName.spool_swamp_south_autumn, RegionName.spool_swamp_south, False, True_()),
        (
            RegionName.spool_swamp_south_spring,
            RegionName.spool_swamp_south_near_gasha_spot,
            False,
            oos_can_break_flowers(True),
        ),
        (
            RegionName.spool_swamp_south_winter,
            RegionName.spool_swamp_south_near_gasha_spot,
            False,
            oos_can_remove_snow(True),
        ),
        (RegionName.spool_swamp_south_summer, RegionName.spool_swamp_south_near_gasha_spot, False, True_()),
        (RegionName.spool_swamp_south_autumn, RegionName.spool_swamp_south_near_gasha_spot, False, True_()),
        # default season only because of the portal
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_south_spring,
            False,
            And(oos_is_default_season("SPOOL_SWAMP", SEASON_SPRING), oos_can_break_flowers(True)),
        ),
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_south_summer,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_SUMMER),
        ),
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_south_autumn,
            False,
            oos_is_default_season("SPOOL_SWAMP", SEASON_AUTUMN),
        ),
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_south_winter,
            False,
            And(oos_is_default_season("SPOOL_SWAMP", SEASON_WINTER), oos_can_remove_snow(True)),
        ),
        (
            RegionName.spool_swamp_south_winter,
            RegionName.spool_swamp_cave,
            False,
            And(oos_can_remove_snow(True), oos_can_remove_rockslide(True)),
        ),
        (RegionName.spool_swamp_south_spring, RegionName.spool_swamp_heart_piece, False, oos_can_swim(True)),
        # NATZU REGION #############################################################################################
        (RegionName.north_horon, RegionName.natzu_west, True, True_()),
        (
            RegionName.moblin_keep_bridge,
            RegionName.moblin_keep,
            True,
            Or(oos_has_flippers(), oos_can_jump_4_wide_liquid(True)),
        ),
        (RegionName.moblin_keep, RegionName.moblin_keep_chest, False, oos_has_bracelet()),
        (RegionName.moblin_keep, RegionName.sunken_city_entrance, False, True_()),
        (RegionName.natzu_river_bank, RegionName.goron_mountain_entrance, True, oos_can_swim(True)),
        # Access to natzu deku is companion specific
        (
            RegionName.natzu_deku,
            RegionName.deku_secret,
            False,
            And(
                oos_can_use_seeds(),
                oos_has_ember_seeds(),
                oos_has_scent_seeds(),
                oos_has_pegasus_seeds(),
                oos_has_gale_seeds(),
                oos_has_mystery_seeds(),
            ),
            bool(options.secret_locations),
        ),
        # SUNKEN CITY ############################################################################################
        (
            RegionName.sunken_city_entrance,
            RegionName.sunken_city,
            True,
            Or(
                oos_has_feather(),
                oos_has_flippers(),
                oos_can_summon_dimitri(),
                oos_is_default_season("SUNKEN_CITY", SEASON_WINTER),
            ),
        ),
        (
            RegionName.sunken_city,
            RegionName.sunken_city_tree,
            False,
            And(
                oos_can_harvest_tree(True),
            ),
        ),
        (
            RegionName.sunken_city,
            RegionName.sunken_city_dimitri,
            False,
            Or(
                oos_can_summon_dimitri(),
                oos_has_bombs(),
            ),
        ),
        (
            # Go back to the entrance, useful when starting/coming from Sunken
            RegionName.sunken_city_dimitri,
            RegionName.sunken_city_entrance,
            False,
            True_(),
        ),
        (
            RegionName.sunken_city,
            RegionName.ingo_trade,
            False,
            Or(Has("Goron Vase"), oos_self_locking_item("Sunken City: Ingo Trade", "Goron Vase")),
        ),
        (
            RegionName.sunken_city,
            RegionName.syrup_trade,
            False,
            And(oos_season_in_sunken_city(SEASON_WINTER), Has("Mushroom")),
        ),
        (RegionName.syrup_trade, RegionName.syrup_shop, False, oos_has_rupees_for_shop("syrupShop")),
        # Use Dimitri to get the tree seeds, using dimitri to get seeds being medium difficulty
        (
            RegionName.sunken_city_dimitri,
            RegionName.sunken_city_tree,
            False,
            And(oos_option_medium_logic(), oos_can_use_seeds()),
        ),
        (
            RegionName.sunken_city_dimitri,
            RegionName.master_divers_challenge,
            False,
            And(oos_has_sword(False), Or(oos_has_feather(), oos_has_flippers())),
        ),
        (
            RegionName.sunken_city_dimitri,
            RegionName.master_divers_reward,
            False,
            Or(Has("Master's Plaque"), oos_self_locking_item("Sunken City: Master's Plaque Trade", "Master's Plaque")),
        ),
        (RegionName.sunken_city_dimitri, RegionName.chest_in_master_divers_cave, False, True_()),
        (
            RegionName.sunken_city,
            RegionName.sunken_city_summer_cave,
            False,
            And(oos_season_in_sunken_city(SEASON_SUMMER), oos_has_flippers(), oos_can_break_bush(False, True)),
        ),
        (
            RegionName.sunken_city,
            RegionName.diver_secret,
            False,
            And(
                oos_has_flippers(),
                Or(
                    And(
                        Has("Swimmer's Ring"),
                        oos_option_medium_logic(),
                    ),
                    oos_option_hard_logic(),
                    oos_has_sword(),
                    oos_has_fools_ore(),
                ),
            ),
            bool(options.secret_locations),
        ),
        (RegionName.mount_cucco, RegionName.sunken_city, False, oos_has_flippers()),
        (
            RegionName.sunken_city,
            RegionName.mount_cucco,
            False,
            And(oos_has_flippers(), oos_season_in_sunken_city(SEASON_SUMMER)),
        ),
        # MT. CUCCO / GORON MOUNTAINS ##############################################################################
        (RegionName.mount_cucco, RegionName.mt_cucco_portal, True, True_()),
        (
            RegionName.mount_cucco,
            RegionName.rightmost_rooster_ledge,
            False,
            And(
                Or(  # to reach the rooster
                    And(
                        oos_season_in_mt_cucco(SEASON_SPRING),
                        Or(
                            oos_can_break_flowers(),
                            Has("Spring Banana"),
                        ),
                    ),
                    oos_option_hard_logic(),
                ),
                oos_has_bracelet(),  # to grab the rooster
            ),
        ),
        (RegionName.rightmost_rooster_ledge, RegionName.mt_cucco_platform_cave, False, True_()),
        (
            RegionName.rightmost_rooster_ledge,
            RegionName.spring_banana_tree,
            False,
            And(
                oos_has_feather(),
                oos_season_in_mt_cucco(SEASON_SPRING),
                Or(  # can harvest tree
                    oos_has_sword(), oos_has_fools_ore()
                ),
            ),
        ),
        (
            RegionName.mount_cucco,
            RegionName.mt_cucco_talons_cave_entrance,
            False,
            oos_season_in_mt_cucco(SEASON_SPRING),
        ),
        (RegionName.mt_cucco_talons_cave_entrance, RegionName.mount_cucco, False, True_()),
        (
            RegionName.mt_cucco_talons_cave_entrance,
            RegionName.talon_trade,
            False,
            And(
                Has("Megaphone"),
                Or(oos_is_default_season("SUNKEN_CITY", SEASON_WINTER, False), oos_can_remove_season(SEASON_WINTER)),
            ),
        ),
        (RegionName.mt_cucco_talons_cave_entrance, RegionName.mt_cucco_heart_piece, False, True_()),
        (
            RegionName.mt_cucco_talons_cave_entrance,
            RegionName.diving_spot_outside_D4,
            False,
            And(
                oos_has_flippers(),
                Or(oos_is_default_season("SUNKEN_CITY", SEASON_WINTER, False), oos_can_remove_season(SEASON_WINTER)),
            ),
        ),
        (
            RegionName.mt_cucco_talons_cave_entrance,
            RegionName.dragon_keyhole,
            False,
            And(
                oos_has_winter(),  # to reach cave
                oos_has_feather(),  # to jump in cave
                oos_has_bracelet(),  # to grab the rooster
            ),
        ),
        (RegionName.dragon_keyhole, RegionName.d4_entrance, False, And(Has("Dragon Key"), oos_has_summer())),
        (RegionName.d4_entrance, RegionName.mt_cucco_talons_cave_entrance, False, True_()),
        (
            RegionName.mount_cucco,
            RegionName.goron_mountain_across_pits,
            False,
            Or(
                Has("Spring Banana"),
                And(
                    oos_option_hard_logic(),
                    oos_can_jump_4_wide_pit(),
                ),
                oos_can_jump_5_wide_pit(),
            ),
        ),
        (
            RegionName.mount_cucco,
            RegionName.goron_blocked_cave_entrance,
            False,
            Or(oos_can_remove_snow(False), Has("Spring Banana")),
        ),
        (RegionName.goron_blocked_cave_entrance, RegionName.mount_cucco, False, oos_can_remove_snow(False)),
        (RegionName.goron_blocked_cave_entrance, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.goron_blocked_cave_entrance, RegionName.goron_mountain, True, oos_has_bracelet()),
        (RegionName.goron_mountain, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.goron_blocked_cave_entrance, RegionName.gorons_gift, False, oos_can_remove_rockslide(False)),
        (
            RegionName.goron_mountain,
            RegionName.biggoron_trade,
            False,
            And(
                oos_can_jump_1_wide_liquid(False),
                Or(
                    Has("Lava Soup"),
                    And(
                        oos_self_locking_item("Goron Mountain: Biggoron Trade", "Lava Soup"),
                        from_option(
                            OracleOfSeasonsIncludeSecretLocations, OracleOfSeasonsIncludeSecretLocations.option_false
                        ),
                    ),
                ),
            ),
        ),
        (
            RegionName.goron_mountain,
            RegionName.chest_in_goron_mountain,
            False,
            And(
                oos_can_jump_3_wide_liquid(),
                Or(
                    oos_has_bombs_for_tiles(),
                    And(  # Bombchu can only destroy the second block, so we need to use cape to jump around the first
                        oos_option_hard_logic(), oos_has_bombchus_for_tiles(), oos_can_use_pegasus_seeds()
                    ),
                    And(oos_option_hell_logic(), oos_has_bombchus_for_tiles(), oos_has_bombchus_for_bombjump()),
                ),
            ),
        ),
        (RegionName.goron_mountain, RegionName.old_man_in_goron_mountain, False, oos_can_use_ember_seeds(False)),
        (
            RegionName.goron_mountain_entrance,
            RegionName.goron_mountain,
            False,
            Or(oos_has_flippers(), oos_can_jump_4_wide_liquid(allow_bombchus=True), oos_has_tight_switch_hook()),
        ),
        (
            RegionName.goron_mountain,
            RegionName.goron_mountain_entrance,
            False,
            Or(
                oos_has_flippers(),
                oos_can_jump_4_wide_liquid(allow_bombchus=True),
                And(
                    # You can't see the other side from this point
                    oos_option_medium_logic(),
                    oos_has_switch_hook(),
                ),
            ),
        ),
        (
            RegionName.goron_mountain_entrance,
            RegionName.temple_remains_lower_stump,
            False,
            Or(
                oos_can_jump_3_wide_pit(),
                And(
                    oos_can_dimitri_clip(),
                    oos_can_jump_2_wide_pit(),
                    Or(
                        # The bombs are actually to clip out of the rock
                        oos_has_bombs_for_bombjump(),
                        oos_has_bombchus_for_bombjump(),
                    ),
                ),
            ),
        ),
        (RegionName.temple_remains_lower_stump, RegionName.goron_mountain_entrance, False, oos_can_jump_3_wide_pit()),
        # TARM RUINS ###############################################################################################
        (RegionName.spool_swamp_north, RegionName.tarm_ruins, False, oos_has_required_jewels()),
        (RegionName.tarm_ruins, RegionName.spool_swamp_north, False, True_()),
        (
            RegionName.tarm_ruins,
            RegionName.lost_woods_top_statue,
            False,
            And(
                Or(
                    oos_season_in_lost_woods(SEASON_SUMMER),
                    And(
                        oos_season_in_lost_woods(SEASON_AUTUMN),
                        oos_option_medium_logic(),
                        oos_has_magic_boomerang(),
                        Or(oos_can_jump_1_wide_pit(False), oos_option_hard_logic()),
                    ),
                ),
                oos_season_in_lost_woods(SEASON_WINTER),
                oos_can_remove_season(SEASON_WINTER),
            ),
        ),
        (
            RegionName.lost_woods_top_statue,
            RegionName.lost_woods_stump,
            False,
            And(
                # Winter has to be in inventory to be here, it allows crossing the water
                oos_has_autumn(),
                oos_can_break_mushroom(False),
            ),
        ),
        (
            RegionName.lost_woods_top_statue,
            RegionName.lost_woods_deku,
            False,
            And(
                oos_has_autumn(),
                Or(oos_can_jump_2_wide_liquid(True), oos_can_swim(False)),
                oos_can_break_mushroom(False),
                oos_has_shield(),
            ),
        ),
        (RegionName.lost_woods_stump, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.lost_woods_stump,
            RegionName.tarm_ruins,
            False,
            And(
                oos_season_in_lost_woods(SEASON_AUTUMN),
                oos_can_break_mushroom(False),
                oos_has_winter(),
                from_option(OracleOfSeasonsTarmGateRequirement, 0),
            ),
        ),
        (
            RegionName.lost_woods_stump,
            RegionName.lost_woods_top_statue,
            False,
            And(
                oos_season_in_lost_woods(SEASON_AUTUMN),
                oos_has_season(SEASON_WINTER),
                Or(
                    oos_has_season(SEASON_SUMMER),
                    And(
                        oos_has_season(SEASON_AUTUMN),
                        oos_option_medium_logic(),
                        oos_has_magic_boomerang(),
                        Or(oos_can_jump_1_wide_pit(False), oos_option_hard_logic()),
                    ),
                ),
            ),
        ),
        (
            RegionName.lost_woods_stump,
            RegionName.lost_woods_phonograph,
            False,
            And(
                Or(
                    oos_can_remove_snow(False),
                    oos_can_remove_season(SEASON_WINTER),
                ),
                oos_can_use_ember_seeds(False),
                Has("Phonograph"),
            ),
        ),
        (RegionName.lost_woods_stump, RegionName.lost_woods, False, oos_can_reach_lost_woods_pedestal(False)),
        # When coming back from the eyeglass lake
        (RegionName.lost_woods, RegionName.lost_woods_stump, False, True_()),
        # To allow reaching the deku if base season is autumn
        (
            RegionName.lost_woods,
            RegionName.lost_woods_deku,
            False,
            And(
                oos_season_in_tarm_ruins(SEASON_AUTUMN),
                CanReachRegion(RegionName.lost_woods_top_statue),
                Or(
                    # A bit tight and diagonal, above water
                    oos_can_jump_3_wide_pit(),
                    oos_can_swim(False),
                ),
                oos_can_break_mushroom(False),
                oos_has_shield(),
            ),
        ),
        # special case for getting to d6 using default season
        (
            RegionName.lost_woods,
            RegionName.d6_sector,
            False,
            And(oos_can_complete_lost_woods_main_sequence(True), oos_option_medium_logic()),
        ),
        (RegionName.lost_woods_stump, RegionName.d6_sector, False, oos_can_complete_lost_woods_main_sequence()),
        (RegionName.d6_sector, RegionName.lost_woods_stump, False, True_()),
        # special case for getting to pedestal using default season
        (
            RegionName.d6_sector,
            RegionName.lost_woods,
            False,
            And(oos_can_reach_lost_woods_pedestal(True), oos_option_medium_logic()),
        ),
        (RegionName.d6_sector, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (RegionName.d6_sector, RegionName.tarm_ruins_tree, False, oos_can_harvest_tree(False)),
        (
            RegionName.d6_sector,
            RegionName.tarm_ruins_under_tree,
            False,
            And(oos_season_in_tarm_ruins(SEASON_AUTUMN), oos_can_break_mushroom(False), oos_can_use_ember_seeds(False)),
        ),
        (
            RegionName.d6_sector,
            RegionName.d6_entrance,
            False,
            And(
                oos_season_in_tarm_ruins(SEASON_WINTER),
                Or(
                    oos_has_shovel(),
                    oos_can_use_ember_seeds(False),
                    And(oos_can_reach_rooster_adventure(), oos_roosters("d6", 1, 0, 0)),
                ),
                oos_season_in_tarm_ruins(SEASON_SPRING),
                oos_can_break_flowers(),
            ),
        ),
        (
            RegionName.d6_sector,
            RegionName.old_man_near_d6,
            False,
            And(
                oos_season_in_tarm_ruins(SEASON_WINTER),
                oos_can_use_ember_seeds(False),
                Or(
                    And(oos_season_in_tarm_ruins(SEASON_SPRING), oos_can_break_flowers()),
                    And(oos_can_reach_rooster_adventure(), oos_roosters("d6", 1, 1, 0)),
                ),
            ),
        ),
        # When coming from D6 entrance, the pillar needs to be broken during spring to be able to go backwards
        (
            RegionName.d6_entrance,
            RegionName.d6_sector,
            False,
            And(oos_is_default_season("TARM_RUINS", SEASON_SPRING), oos_can_break_flowers()),
        ),
        # SAMASA DESERT ######################################################################################
        (RegionName.suburbs, RegionName.samasa_desert, False, Has("_met_pirates")),
        (RegionName.samasa_desert, RegionName.samasa_desert_pit, False, oos_has_bracelet()),
        (RegionName.samasa_desert, RegionName.samasa_desert_chest, False, oos_has_flippers()),
        (
            RegionName.samasa_desert,
            RegionName.samasa_desert_scrub,
            False,
            oos_has_rupees_for_shop("samasaCaveScrub"),
            bool(options.shuffle_business_scrubs),
        ),
        (RegionName.samasa_desert, RegionName.subrosia_pirates_sector, False, True_()),
        # d11 in samasa rules
        (
            RegionName.samasa_desert,
            RegionName.d11_entrance,
            True,
            True_(),
            options.linked_heros_cave.is_samasa,
        ),
        (
            RegionName.samasa_desert,
            RegionName.d11_alt_entrance,
            False,
            oos_can_break_bush(),
            options.linked_heros_cave.is_alt_entrance,
        ),
        # TEMPLE REMAINS ####################################################################################
        (RegionName.temple_remains_lower_stump, RegionName.maple_encounter, False, oos_can_meet_maple()),
        (
            RegionName.temple_remains_lower_stump,
            RegionName.temple_remains_upper_stump,
            False,
            And(
                oos_has_feather(),  # Require feather in case volcano has erupted
                oos_can_break_bush(False, False),
                Or(
                    Has("_triggered_volcano"),  # Volcano rule
                    And(  # Winter rule
                        oos_season_in_temple_remains(SEASON_WINTER),
                        oos_can_remove_snow(False),
                        oos_can_jump_6_wide_pit(),
                    ),
                    And(  # Summer rule
                        oos_season_in_temple_remains(SEASON_SUMMER), oos_can_jump_6_wide_pit()
                    ),
                    And(  # Spring rule
                        oos_season_in_temple_remains(SEASON_SPRING), oos_can_break_flowers(), oos_can_jump_6_wide_pit()
                    ),
                    oos_season_in_temple_remains(SEASON_AUTUMN),  # Autumn rule
                ),
            ),
        ),
        (
            RegionName.temple_remains_upper_stump,
            RegionName.temple_remains_lower_stump,
            False,
            And(
                oos_has_feather(),  # Require feather in case volcano has erupted
                Or(
                    Has("_triggered_volcano"),  # Volcano rule
                    oos_season_in_temple_remains(SEASON_WINTER),  # Winter rule
                    And(  # Summer rule
                        oos_season_in_temple_remains(SEASON_SUMMER),
                        oos_can_break_bush(False, False),
                        oos_can_jump_6_wide_pit(),
                    ),
                    And(  # Spring rule
                        oos_season_in_temple_remains(SEASON_SPRING),
                        oos_can_break_flowers(),
                        oos_can_break_bush(False, False),
                        oos_can_jump_6_wide_pit(),
                    ),
                    And(  # Autumn rule
                        oos_season_in_temple_remains(SEASON_AUTUMN), oos_can_break_bush()
                    ),
                ),
            ),
        ),
        (
            RegionName.temple_remains_lower_stump,
            RegionName.temple_remains_lower_portal_access,
            False,
            And(Has("_triggered_volcano"), oos_has_feather()),
        ),
        (
            RegionName.temple_remains_upper_stump,
            RegionName.temple_remains_lower_portal_access,
            False,
            And(
                oos_has_feather(),
                Or(
                    oos_has_winter(),
                    Has("_triggered_volcano"),
                    And(
                        # You can only reach the portal from here with the default Winter,
                        # if you made the zipper jump first
                        # Otherwise you would have turned it Autumn first
                        oos_season_in_temple_remains(SEASON_WINTER),
                        oos_can_remove_snow(False),
                        oos_can_break_bush(False),
                        oos_can_jump_6_wide_pit(),
                    ),
                ),
            ),
        ),
        (RegionName.temple_remains_lower_portal_access, RegionName.temple_remains_lower_portal, True, True_()),
        # There is an added ledge in rando that enables jumping from the portal down to the stump,
        # whatever the season is
        (RegionName.temple_remains_lower_portal, RegionName.temple_remains_lower_stump, False, True_()),
        (
            RegionName.temple_remains_lower_stump,
            RegionName.temple_remains_heart_piece,
            False,
            And(
                Has("_triggered_volcano"),
                oos_can_jump_2_wide_liquid(),
                oos_can_remove_rockslide(False),
            ),
        ),
        (
            RegionName.temple_remains_lower_stump,
            RegionName.temple_remains_upper_portal,
            False,
            And(
                Has("_triggered_volcano"),
                oos_season_in_temple_remains(SEASON_SUMMER),
                oos_can_jump_2_wide_liquid(),
                Or(oos_has_magnet_gloves(), oos_can_jump_6_wide_pit()),
            ),
        ),
        (
            RegionName.temple_remains_upper_portal,
            RegionName.temple_remains_lower_stump,
            False,
            And(Has("_triggered_volcano"), oos_can_jump_1_wide_liquid(False)),
        ),
        (
            RegionName.temple_remains_upper_portal,
            RegionName.temple_remains_upper_stump,
            False,
            oos_can_jump_1_wide_pit(False),
        ),
        (
            RegionName.temple_remains_upper_portal,
            RegionName.temple_remains_lower_portal_access,
            False,
            And(
                oos_has_feather(),  # Require feather in case volcano has erupted
                Or(Has("_triggered_volcano"), oos_is_default_season("TEMPLE_REMAINS", SEASON_WINTER)),
            ),
        ),
        # ONOX CASTLE #############################################################################################
        (RegionName.maku_tree, RegionName.maku_seed, False, oos_has_essences_for_maku_seed()),
        (RegionName.maku_tree, RegionName.maku_tree_3_essences, False, oos_has_essences(3)),
        (RegionName.maku_tree, RegionName.maku_tree_5_essences, False, oos_has_essences(5)),
        (RegionName.maku_tree, RegionName.maku_tree_7_essences, False, oos_has_essences(7)),
        (RegionName.north_horon, RegionName.d9_entrance, False, CanReachRegion(RegionName.maku_seed)),
        (
            RegionName.d9_entrance,
            RegionName.onox_beaten,
            False,
            And(
                oos_can_kill_armored_enemy(True, True),
                oos_can_kill_facade(),
                oos_has_sword(False),
                oos_has_feather(),
                Or(oos_option_hard_logic(), oos_has_rod()),
                oos_has_hearts_by_difficulty(8, 6, 4),
            ),
        ),
        (
            RegionName.onox_beaten,
            RegionName.ganon_beaten,
            False,
            Or(
                And(
                    # casual rules
                    oos_has_noble_sword(),
                    oos_has_seed_thrower(),
                    oos_can_use_ember_seeds(False),
                    oos_can_use_mystery_seeds(),
                ),
                And(
                    oos_option_medium_logic(),
                    oos_has_sword(False),
                    Or(
                        # all seeds damage Twinrova phase 2
                        oos_has_seed_thrower(),
                        And(
                            oos_option_hard_logic(),
                            oos_can_use_seeds(),
                            # satchel can't use pegasus to damage, but all others work
                            Or(
                                oos_has_ember_seeds(),
                                oos_has_mystery_seeds(),
                                oos_has_scent_seeds(),
                                oos_has_gale_seeds(),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        # GOLDEN BEASTS #############################################################################################
        (
            RegionName.d0_entrance,
            RegionName.golden_darknut,
            False,
            And(
                Or(
                    oos_is_default_season("WESTERN_COAST", SEASON_SPRING),
                    And(
                        oos_season_in_western_coast(SEASON_SPRING),
                        Has("Pirate's Bell"),
                        Has("_met_pirates"),
                    ),
                ),
                Or(
                    oos_has_sword(),
                    oos_has_fools_ore(),
                    oos_can_summon_dimitri(),
                    And(oos_option_hard_logic(), oos_has_cane()),
                ),
            ),
        ),
        (
            RegionName.lost_woods_top_statue,
            RegionName.golden_lynel,
            False,
            Or(oos_has_sword(), oos_has_fools_ore(), And(oos_option_hard_logic(), oos_has_cane())),
        ),
        (
            RegionName.lost_woods_stump,
            RegionName.golden_lynel,
            False,
            And(
                # We can assume coming from d6 or pedestal otherwise rule above applies
                oos_season_in_lost_woods(SEASON_AUTUMN),
                oos_can_break_mushroom(False),
                oos_has_winter(),
                Or(oos_has_sword(), oos_has_fools_ore(), And(oos_option_hard_logic(), oos_has_cane())),
            ),
        ),
        (
            RegionName.d2_entrance,
            RegionName.golden_moblin,
            False,
            And(
                oos_season_in_central_woods_of_winter(SEASON_AUTUMN),
                Or(
                    oos_has_sword(),
                    oos_has_fools_ore(),
                    # Moblin has the interesting property of being one-shottable using an ember seed
                    And(oos_option_medium_logic(), oos_can_use_ember_seeds(True)),
                    oos_can_summon_dimitri(),
                    And(oos_option_hard_logic(), oos_has_cane()),
                ),
            ),
        ),
        (
            RegionName.spool_swamp_south_summer,
            RegionName.golden_octorok,
            False,
            Or(
                oos_has_sword(),
                oos_has_fools_ore(),
                oos_can_summon_dimitri(),
                And(oos_option_hard_logic(), oos_has_cane()),
            ),
        ),
        # GASHA TREES #############################################################################################
        (
            RegionName.horon_village,
            RegionName.horon_gasha_spot,
            False,
            True_(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.impas_house,
            RegionName.impa_gasha_spot,
            False,
            oos_can_break_bush(True, True),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.suburbs,
            RegionName.suburbs_gasha_spot,
            False,
            oos_can_break_bush(True, True),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.ghastly_stump,
            RegionName.holodrum_plain_gasha_spot,
            False,
            And(
                oos_can_break_bush(True, False),  # Zoras make the bombchus not viable
                oos_has_shovel(),
            ),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.d1_island,
            RegionName.holodrum_plain_island_gasha_spot,
            False,
            And(
                oos_can_swim(True),
                Or(
                    oos_can_break_bush(False, False),
                    oos_can_summon_dimitri(),  # Only Dimitri can be brought here
                ),
            ),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.floodgate_keyhole,
            RegionName.spool_swamp_north_gasha_spot,
            False,
            oos_has_bracelet(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.spool_swamp_south_near_gasha_spot,
            RegionName.spool_swamp_south_gasha_spot,
            False,
            oos_has_bracelet(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.sunken_city,
            RegionName.sunken_city_gasha_spot,
            False,
            And(
                oos_season_in_sunken_city(SEASON_SUMMER),
                oos_can_swim(False),
                oos_can_break_bush(False, False),  # Technically doable by positioning link with a sword
            ),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.sunken_city_dimitri,
            RegionName.sunken_city_gasha_spot,
            False,
            True_(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.goron_mountain_entrance,
            RegionName.goron_mountain_left_gasha_spot,
            False,
            oos_has_shovel(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.goron_mountain_entrance,
            RegionName.goron_mountain_right_gasha_spot,
            False,
            oos_has_bracelet(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.d5_stump,
            RegionName.eyeglass_lake_gasha_spot,
            False,
            And(
                oos_has_shovel(),
                oos_can_break_bush(True, True),
            ),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.mount_cucco,
            RegionName.mt_cucco_gasha_spot,
            False,
            And(
                oos_season_in_mt_cucco(SEASON_AUTUMN),
                oos_can_break_mushroom(False),
            ),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.d6_sector,
            RegionName.tarm_ruins_gasha_spot,
            False,
            oos_has_shovel(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.samasa_desert,
            RegionName.samasa_desert_gasha_spot,
            False,
            True_(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.western_coast_after_ship,
            RegionName.western_coast_gasha_spot,
            False,
            True_(),
            options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.north_horon,
            RegionName.onox_gasha_spot,
            False,
            oos_has_shovel(),
            options.deterministic_gasha_locations >= 1,
        ),
        (RegionName.natzu_west, RegionName.natzu_west_ricky, True, True_(), options.animal_companion == "ricky"),
        (
            RegionName.natzu_west_ricky,
            RegionName.natzu_east_ricky,
            True,
            oos_can_summon_ricky(),
            options.animal_companion == "ricky",
        ),
        (
            RegionName.natzu_east_ricky,
            RegionName.sunken_city_entrance,
            True,
            True_(),
            options.animal_companion == "ricky",
        ),
        (
            RegionName.natzu_east_ricky,
            RegionName.moblin_keep_bridge,
            False,
            True_(),
            options.animal_companion == "ricky",
        ),
        (
            RegionName.natzu_east_ricky,
            RegionName.natzu_river_bank,
            True,
            oos_can_summon_ricky(),
            options.animal_companion == "ricky",
        ),
        (
            RegionName.natzu_east_ricky,
            RegionName.natzu_deku,
            False,
            oos_can_break_bush(True),
            bool(options.animal_companion == "ricky" and options.secret_locations),
        ),
        (RegionName.natzu_west, RegionName.natzu_west_dimitri, True, True_(), options.animal_companion == "dimitri"),
        (
            RegionName.natzu_west_dimitri,
            RegionName.natzu_east_dimitri,
            True,
            oos_can_swim(True),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.natzu_east_dimitri,
            RegionName.sunken_city_entrance,
            True,
            oos_can_jump_1_wide_pit(False),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.natzu_east_dimitri,
            RegionName.natzu_region_across_water,
            False,
            oos_can_jump_5_wide_liquid(),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.natzu_east_dimitri,
            RegionName.moblin_keep_bridge,
            False,
            Or(oos_can_summon_dimitri(), And(oos_option_medium_logic(), oos_has_flippers(), Has("Swimmer's Ring"))),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.natzu_east_dimitri,
            RegionName.natzu_river_bank,
            True,
            True_(),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.natzu_west_dimitri,
            RegionName.natzu_deku,
            False,
            oos_can_summon_dimitri(),
            bool(options.animal_companion == "dimitri" and options.secret_locations),
        ),
        (
            RegionName.sunken_city_entrance,
            RegionName.moblin_keep,
            False,
            oos_can_dimitri_clip(),
            options.animal_companion == "dimitri",
        ),
        (
            RegionName.moblin_keep_bridge,
            RegionName.natzu_east_dimitri,
            False,
            oos_can_swim(True),
            options.animal_companion == "dimitri",
        ),
        (RegionName.natzu_west, RegionName.natzu_west_moosh, True, True_(), options.animal_companion == "moosh"),
        (
            RegionName.natzu_west_moosh,
            RegionName.natzu_east_moosh,
            True,
            Or(
                oos_can_summon_moosh(),
                And(oos_option_medium_logic(), oos_can_break_bush(True), oos_can_jump_3_wide_pit()),
            ),
            options.animal_companion == "moosh",
        ),
        (
            RegionName.natzu_east_moosh,
            RegionName.sunken_city_entrance,
            True,
            Or(
                oos_can_summon_moosh(),
                oos_can_jump_3_wide_liquid(),  # Not a liquid, but it's a diagonal jump so that's the same
            ),
            options.animal_companion == "moosh",
        ),
        (
            RegionName.natzu_east_moosh,
            RegionName.moblin_keep_bridge,
            False,
            Or(oos_can_summon_moosh(), And(oos_can_break_bush(), oos_can_jump_3_wide_pit())),
            options.animal_companion == "moosh",
        ),
        (RegionName.natzu_east_moosh, RegionName.natzu_river_bank, True, True_(), options.animal_companion == "moosh"),
        (
            RegionName.natzu_west_moosh,
            RegionName.natzu_deku,
            False,
            Or(
                oos_can_summon_moosh(),
                oos_can_jump_4_wide_liquid(),
                And(oos_can_jump_4_wide_pit(), oos_can_break_bush()),
            ),
            bool(options.animal_companion == "moosh" and options.secret_locations),
        ),
        (
            RegionName.d4_entrance,
            RegionName.dragon_keyhole,
            False,
            And(
                # Rule specifically to get to the dragon keyhole from a side entrance,
                # only useful for rooster's adventure
                oos_is_default_season("SUNKEN_CITY", SEASON_WINTER),  # to reach cave
                oos_has_feather(),  # to jump in cave
                oos_has_bracelet(),  # to grab the rooster
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        # Item assumptions for the rest of that logic :
        # Bracelet
        # Feather
        (
            RegionName.dragon_keyhole,
            RegionName.rooster_adventure,
            False,
            And(oos_has_gale_seeds(), oos_has_satchel(), Or(oos_has_shovel(), Has("Spring Banana"))),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.goron_mountain_entrance,
            False,
            oos_roosters("cucco mountain", 0, 0, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.moblin_keep,
            False,
            Or(
                And(oos_roosters("sunken", 1, 1, 0), oos_is_companion_ricky()),
                And(
                    oos_roosters("horon", 1, 1, 0),
                    Or(oos_has_flute(), And(oos_is_companion_moosh(), oos_can_jump_3_wide_pit())),
                ),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.sunken_city_entrance,
            False,
            oos_roosters("sunken", 0, 0, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.sunken_city_gasha_spot,
            False,
            And(oos_roosters("sunken", 1, 0, 1), oos_season_in_sunken_city(SEASON_WINTER)),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell
            and options.deterministic_gasha_locations >= 1,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.syrup_trade,
            False,
            And(oos_roosters("sunken", 1, 0, 1), Has("Mushroom")),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.suburbs,
            False,
            oos_roosters("suburbs", 0, 0, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.eastern_suburbs_spring_cave,
            False,
            And(
                oos_roosters("suburbs", 1, 0, 1),
                oos_season_in_eastern_suburbs(SEASON_SPRING),
                Or(oos_has_magnet_gloves(), oos_can_jump_3_wide_pit()),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.windmill_heart_piece,
            False,
            oos_roosters("suburbs", 1, 1, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.samasa_desert_chest,
            False,
            And(
                oos_roosters("suburbs", 1, 1, 0),
                Has("_met_pirates"),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.moblin_road,
            False,
            oos_roosters("moblin road", 0, 0, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.hollys_house,
            False,
            oos_roosters("moblin road", 1, 1, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.horon_heart_piece,
            False,
            oos_roosters("horon", 1, 1, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.graveyard_heart_piece,
            False,
            And(
                oos_roosters("horon", 1, 1, 0),
                Has("_met_pirates"),
                Has("Pirate's Bell"),
                oos_is_default_season("WESTERN_COAST", SEASON_SUMMER),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.spool_swamp_north,
            False,
            oos_roosters("swamp", 0, 0, 0),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.lost_woods_deku,
            False,
            And(
                oos_roosters("swamp", 1, 1, 0),
                oos_has_required_jewels(),
                Or(oos_season_in_lost_woods(SEASON_SUMMER), CanReachRegion(RegionName.lost_woods_top_statue)),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.spool_swamp_cave,
            False,
            Or(
                And(
                    oos_can_swim(True),
                    oos_roosters("horon", 0, 0, 0),
                ),
                And(
                    # We can assume jump 3 holes here, coming from the north
                    Has("Floodgate Key"),
                    Or(
                        oos_is_default_season("SPOOL_SWAMP", SEASON_SPRING, False), oos_can_remove_season(SEASON_SPRING)
                    ),
                    oos_roosters("swamp", 0, 0, 0),
                ),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.temple_remains_upper_stump,
            False,
            And(
                oos_can_jump_3_wide_pit(),
                oos_roosters("cucco mountain", 0, 0, 0),
                Or(
                    # autumn doesn't matter since regular logic already covers that case
                    oos_season_in_temple_remains(SEASON_SUMMER),
                    And(oos_season_in_temple_remains(SEASON_WINTER), oos_has_shovel()),
                    And(oos_season_in_temple_remains(SEASON_SPRING), oos_can_break_flowers()),
                ),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
        (
            RegionName.rooster_adventure,
            RegionName.temple_remains_upper_portal,
            False,
            And(
                Has("_triggered_volcano"),
                oos_can_jump_3_wide_pit(),
                oos_roosters("cucco mountain", 1, 1, 0),
                Or(oos_has_magnet_gloves(), oos_can_jump_6_wide_pit()),
            ),
            options.logic_difficulty == OracleOfSeasonsLogicDifficulty.option_hell,
        ),
    ]


def make_gasha_logic(world: OracleOfSeasonsWorld) -> list[LogicLine]:
    rules: list[LogicLine] = []
    previous_region = world.origin_region_name
    for i in range(world.options.deterministic_gasha_locations):
        new_region = GASHA_REGIONS[i]
        rules.append((previous_region, new_region, False, oos_can_harvest_gasha(i + 1)))
    return rules
