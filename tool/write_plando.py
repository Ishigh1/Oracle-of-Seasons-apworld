import json

from worlds.tloz_oos.data.locations import LOCATIONS_DATA

plando = []
for location in LOCATIONS_DATA:
    data = LOCATIONS_DATA[location]
    if "conditional" not in data:
        if data["vanilla_item"] != "Filler Item":
            plando.append({
                "item": data["vanilla_item"],
                "location": location,
                "from_pool": True,
                "world": True
            })
print(json.dumps(plando, indent=4))
