import json
import argparse

# TODO: Need to merge cards with printing in multiple sets
# TODO: Add intial printing rarity
# Should do something like with card types, keep list of all sets with printings

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
    # Check that we haven't already added the card to the list
    card_tuple = tuple((card["name"], card["color"]))
    if card_tuple in card_set:
        continue
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
    card_dict.update({"set_id": card["set_id"]})

    card_list.append(card_dict)

# Write JSON file with cards
with open("cards.json", mode="w", encoding="utf-8") as f:
    json.dump(card_list, f, indent=2)
