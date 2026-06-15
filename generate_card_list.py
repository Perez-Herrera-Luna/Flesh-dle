import json
import argparse


def find_match_index(card_name: str, card_color: str, search_list: list[dict]) -> int:
    for i, card_i in enumerate(search_list):
        if card_name == card_i["name"] and card_color == card_i["color"]:
            return i
    return -1


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
card_set = set()
card_list = list()
for card in cards:
    # Check that we haven't already added the current card to the list
    card_tuple = tuple((card["name"], card["color"]))

    if card_tuple in card_set:
        # Card already exists in set but we want to append set_id
        match_index = find_match_index(card["name"], card["color"], card_list)
        card_list[match_index]["set_id"].add(card["set_id"])
        card_list[match_index]["rarity"].add(card["rarity"])

        # set_id has been updates, no need to create a new entry
        continue

    # Add name & color tuple to set for duplicate identification
    card_set.add(card_tuple)

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
    card_dict.update({"set_id": set([card["set_id"]])})
    card_dict.update({"card_keywords": card["card_keywords"]})
    card_dict.update({"rarity": set([card["rarity"]])})

    card_list.append(card_dict)


# set_id is currently a set and needs to be cast to a list for writing out as JSON
for card in card_list:
    card.update({"set_id": list(card["set_id"])})
    card.update({"rarity": list(card["rarity"])})

# Write JSON file with cards
with open("cards.json", mode="w", encoding="utf-8") as f:
    json.dump(card_list, f, indent=2)
