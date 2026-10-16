import random
from typing import Any

from ...data.items import RING_LIST
from ...data.locations import LOCATIONS_DATA


def add_vanilla_items(patch_data: dict[str, Any]) -> None:
    patch_locations_data = patch_data["locations"]
    for location_name, location_data in LOCATIONS_DATA.items():
        if location_name in patch_locations_data:
            continue
        if "owl_id" in location_data:
            continue
        vanilla_item = location_data["vanilla_item"]
        if vanilla_item == "Filler Item":
            vanilla_item = "Friendship Ring"
        elif vanilla_item == vanilla_item == "Random Ring":
            vanilla_item = random.choice(RING_LIST)
        patch_locations_data[location_name] = {"item": vanilla_item}
