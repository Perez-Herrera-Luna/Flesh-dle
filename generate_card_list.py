import json
import argparse

# Argument Parser
parser = argparse.ArgumentParser(
    prog="GenerateCardList",
    description="Generate a JSON file with every card and its properties",
)
parser.add_argument("filename")
args = parser.parse_args()

# Read in raw card list
with open(args.filename, mode="r", encoding="utf-8") as read_file:
    cards = json.load(read_file)


# Form list with every card + color
card_list = list()
for card in cards:
    # Form the list element
    card_dict = dict()
    card_dict.update({"name": card["name"]})
    card_dict.update({"color": card["color"]})
    card_dict.update({"pitch": card["pitch"]})
    card_dict.update({"cost": card["cost"]})
    card_dict.update({"power": card["power"]})
    card_dict.update({"defense": card["defense"]})
    card_dict.update({"health": card["health"]})
    card_dict.update({"intelligence": card["intelligence"]})
    card_dict.update({"types": card["types"]})
    card_dict.update({"card_keywords": card["card_keywords"]})

    # Initialize empty sets for elements that vary with multiple printings
    card_dict.update({"set_id": set()})
    card_dict.update({"rarity": set()})

    # Add elements that vary with multiple printings
    for printing in card["printings"]:
        card_dict["set_id"].add(printing["set_id"])
        card_dict["rarity"].add(printing["rarity"])

    card_list.append(card_dict)


# Convert non-unique elements to lists for writing as JSON
for card in card_list:
    card.update({"set_id": list(card["set_id"])})
    card.update({"rarity": list(card["rarity"])})

# Write JSON file with cards
with open("cards.json", mode="w", encoding="utf-8") as f:
    json.dump(card_list, f, indent=2)
