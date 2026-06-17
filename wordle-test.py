import json
import random
from prettytable import PrettyTable
from termcolor import colored

import lookup

# TODO: Move these lookup methods to their own module


# Read in cards
with open("cards.json", mode="r", encoding="utf-8") as read_file:
    cards = json.load(read_file)

# Pick random card
random.seed()
random_num = random.randint(0, len(cards))
random_card = cards[random_num]

# Print random card for testing
print(random_card["name"])
print(random_card["color"])

# Initialize table
table = PrettyTable(max_width=10)
table.field_names = [
    "Name",
    "Color",
    "Pitch",
    "Cost",
    "Power",
    "Defense",
    "Health",
    "Intelligence",
    "Types",
    "Set",
    "Keywords",
    "Rarity",
]

# Guess cards
card_guess = lookup.guess_card(cards)
while card_guess != random_card:
    # Guess was incorrect
    print(colored("Incorrect guess", "red"))

    # Reveal card info
    name_symbol = lookup.match_name(card_guess["name"], random_card["name"])
    color_symbol = lookup.match_color(card_guess["color"], random_card["color"])
    pitch_symbol = lookup.match_pitch(card_guess["pitch"], random_card["pitch"])
    cost_symbol = lookup.match_cost(card_guess["cost"], random_card["cost"])
    power_symbol = lookup.match_power(card_guess["power"], random_card["power"])
    defense_symbol = lookup.match_defense(card_guess["defense"], random_card["defense"])
    health_symbol = lookup.match_health(card_guess["health"], random_card["health"])
    intelligence_symbol = lookup.match_intelligence(
        card_guess["intelligence"], random_card["intelligence"]
    )
    types_symbol = lookup.match_types(card_guess["types"], random_card["types"])
    set_id_symbol = lookup.match_set_id(card_guess["set_id"], random_card["set_id"])
    card_keywords_symbol = lookup.match_card_keywords(
        card_guess["card_keywords"], random_card["card_keywords"]
    )
    rarity_symbol = lookup.match_rarity(card_guess["rarity"], random_card["rarity"])

    table.add_row(
        [
            name_symbol,
            color_symbol,
            pitch_symbol,
            cost_symbol,
            power_symbol,
            defense_symbol,
            health_symbol,
            intelligence_symbol,
            types_symbol,
            set_id_symbol,
            card_keywords_symbol,
            rarity_symbol,
        ]
    )
    print(table)

    # Obtain new card guess
    card_guess = lookup.guess_card(cards)

    # Check if guess is correct
    if card_guess == random_card:
        print(colored("Card correctly guessed", "green"))
