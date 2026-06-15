import json
import random
import re
from prettytable import PrettyTable
from termcolor import colored

# TODO: Move these lookup methods to their own module


# Returns the card that matches card_name and card_color if it exists. Return an empty dict otherwise
def lookup_card(card_name: str, card_color: str, card_list: list) -> dict:
    for card in card_list:
        # TODO: Replace with binary search, might need to sort cards truly alphabetically by name & color
        if card_name == card["name"] and card_color == card["color"]:
            return card

    return dict()


# Returns a valid card guess from the user
def guess_card(card_list) -> dict:
    card_name = input()
    card_color = input()

    card = lookup_card(card_name, card_color, card_list)
    while card == dict():
        print(colored("No such card exists", "yellow"))
        card_name = input()
        card_color = input()
        card = lookup_card(card_name, card_color, card_list)

    return card


def is_numerical_comparison(property1: str, property2: str) -> bool:
    return property1.isdigit() and property2.isdigit()


def match_name(name1: str, name2: str) -> str:
    if name1 == name2:
        return name1 + colored("✓", "green")

    return name1 + colored("X", "red")


def match_color(color1: str, color2: str) -> str:
    if color1 == color2:
        return colored(color1 + " ✓", "green")

    return colored(color1 + " X", "red")


def match_pitch(pitch1: str, pitch2: str) -> str:
    if pitch1 == pitch2:
        return colored(pitch1 + "✓", "green")

    if is_numerical_comparison(pitch1, pitch2):
        numeric_pitch1, numeric_pitch2 = int(pitch1), int(pitch2)

        if numeric_pitch1 < numeric_pitch2:
            return colored(pitch1 + "↑", "yellow")

        return colored(pitch1 + "↓", "yellow")

    return colored(pitch1 + "X", "red")


def match_cost(cost1: str, cost2: str) -> str:
    if cost1 == cost2:
        return colored(cost1 + "✓", "green")

    if is_numerical_comparison(cost1, cost2):
        numeric_cost1, numeric_cost2 = int(cost1), int(cost2)

        if numeric_cost1 < numeric_cost2:
            return colored(cost1 + "↑", "yellow")

        return colored(cost1 + "↓", "yellow")

    return colored(cost1 + "X", "red")


def match_power(power1: str, power2: str) -> str:
    if power1 == power2:
        return colored(power1 + "✓", "green")

    if is_numerical_comparison(power1, power2):
        numeric_power1, numeric_power2 = int(power1), int(power2)

        if numeric_power1 < numeric_power2:
            return colored(power1 + "↑", "yellow")

        return colored(power1 + "↓", "yellow")

    return colored(power1 + "X", "red")


def match_defense(defense1: str, defense2: str) -> str:
    if defense1 == defense2:
        return colored(defense1 + "✓", "green")

    if is_numerical_comparison(defense1, defense2):
        numeric_defense1, numeric_defense2 = int(defense1), int(defense2)

        if numeric_defense1 < numeric_defense2:
            return colored(defense1 + "↑", "yellow")

        return colored(defense1 + "↓", "yellow")

    return colored(defense1 + "X", "red")


def match_health(health1: str, health2: str) -> str:
    if health1 == health2:
        return colored(health1 + "✓", "green")

    if is_numerical_comparison(health1, health2):
        numeric_health1, numeric_health2 = int(health1), int(health2)

        if numeric_health1 < numeric_health2:
            return colored(health1 + "↑", "yellow")

        return colored(health1 + "↓", "yellow")

    return colored(health1 + "X", "red")


def match_intelligence(intelligence1: str, intelligence2: str) -> str:
    if intelligence1 == intelligence2:
        return colored(intelligence1 + "✓", "green")

    if is_numerical_comparison(intelligence1, intelligence2):
        numeric_intelligence1, numeric_intelligence2 = int(intelligence1), int(
            intelligence2
        )

        if numeric_intelligence1 < numeric_intelligence2:
            return colored(intelligence1 + "↑", "yellow")

        return colored(intelligence1 + "↓", "yellow")

    return colored(intelligence1 + "X", "red")


def match_types(types1: list[str], types2: list[str]) -> str:
    if set(types1) == set(types2):
        return str(types1) + colored("✓", "green")

    if set(types1) & set(types2):
        return str(types1) + colored("~", "yellow")

    return str(types1) + colored("X", "red")


def match_set_id(set_id1: list[str], set_id2: list[str]) -> str:
    if set(set_id1) == set(set_id2):
        return str(set_id1) + colored("✓", "green")

    if set(set_id1) & set(set_id2):
        return str(set_id1) + colored(" ~", "yellow")

    # TODO: Consider using lookup table to match set codes to names and to order sets by chronological release
    return str(set_id1) + colored("X", "red")


def match_card_keywords(card_keywords1: list[str], card_keywords2: list[str]) -> str:
    # Remove numbers and trailing whitespace
    clean_keywords1 = [normalize_keyword(keyword) for keyword in card_keywords1]
    clean_keywords2 = [normalize_keyword(keyword) for keyword in card_keywords2]

    if set(clean_keywords1) == set(clean_keywords2):
        return str(card_keywords1) + colored("✓", "green")

    if set(clean_keywords1) & set(clean_keywords2):
        return str(card_keywords1) + colored("~", "yellow")

    return str(card_keywords1) + colored("X", "red")


def match_rarity(rarity1: list[str], rarity2: list[str]) -> str:
    if set(rarity1) == set(rarity2):
        return str(rarity1) + colored("✓", "green")

    if set(rarity1) & set(rarity2):
        return str(rarity1) + colored("~", "yellow")

    return str(rarity1) + colored("X", "red")


def normalize_keyword(keyword: str) -> str:
    return re.sub(r"\s+\d+$", "", keyword)


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
card_guess = guess_card(cards)
while card_guess != random_card:
    # Guess was incorrect
    print(colored("Incorrect guess", "red"))

    # Reveal card info
    name_symbol = match_name(card_guess["name"], random_card["name"])
    color_symbol = match_color(card_guess["color"], random_card["color"])
    pitch_symbol = match_pitch(card_guess["pitch"], random_card["pitch"])
    cost_symbol = match_cost(card_guess["cost"], random_card["cost"])
    power_symbol = match_power(card_guess["power"], random_card["power"])
    defense_symbol = match_defense(card_guess["defense"], random_card["defense"])
    health_symbol = match_health(card_guess["health"], random_card["health"])
    intelligence_symbol = match_intelligence(
        card_guess["intelligence"], random_card["intelligence"]
    )
    types_symbol = match_types(card_guess["types"], random_card["types"])
    set_id_symbol = match_set_id(card_guess["set_id"], random_card["set_id"])
    card_keywords_symbol = match_card_keywords(
        card_guess["card_keywords"], random_card["card_keywords"]
    )
    rarity_symbol = match_rarity(card_guess["rarity"], random_card["rarity"])

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
    card_guess = guess_card(cards)

    # Check if guess is correct
    if card_guess == random_card:
        print(colored("Card correctly guessed", "green"))
