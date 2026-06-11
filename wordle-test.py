import json
import random
from prettytable import PrettyTable


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
        print("No such card exists")
        card_name = input()
        card_color = input()
        card = lookup_card(card_name, card_color, card_list)

    return card


def match_name(name1, name2) -> str:
    if name1 == name2:
        return "✓"

    return "X"


def match_color(color1, color2) -> str:
    if color1 == color2:
        return "✓"

    return "X"


# Pitch is always interpreted as a string. Cards can have no/null pitch. Such pitch is ""
# Current comparions are not sufficient because they assume numerical comparison
# TODO: Need to retool this and every other psuedo numerical comparison
def match_pitch(pitch1, pitch2) -> str:
    if pitch1 == pitch2:
        return "✓"
    elif pitch1 < pitch2:
        return "↑"
    elif pitch1 > pitch2:
        return "↓"

    return "X"


# Cards can have no/null cost
def match_cost(cost1, cost2) -> str:
    if cost1 == cost2:
        return "✓"
    elif cost1 < cost2:
        return "↑"

    return "↓"


# Cards can have no/null power
def match_power(power1, power2) -> str:
    if power1 == power2:
        return "✓"
    elif power1 < power2:
        return "↑"

    return "↓"


# Cards can have no/null defense
def match_defense(defense1, defense2) -> str:
    if defense1 == defense2:
        return "✓"
    elif defense1 < defense2:
        return "↑"

    return "↓"


# Cards can have no/null health
def match_health(health1, health2) -> str:
    if health1 == health2:
        return "✓"
    elif health1 < health2:
        return "↑"

    return "↓"


# Cards can have no/null intelligence
def match_intelligence(intelligence1, intelligence2) -> str:
    if intelligence1 == intelligence2:
        return "✓"
    elif intelligence1 < intelligence2:
        return "↑"

    return "↓"


# TODO: Match card types (e.g. Light, Illusionist, Instant, Aura)


def match_set_id(set_id1, set_id2) -> str:
    if set_id1 == set_id2:
        return "✓"

    # TODO: Consider using lookup table to match set codes to names and to order sets by chronological release
    return "X"


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
table = PrettyTable()
table.field_names = [
    "Name",
    "Color",
    "Pitch",
    "Cost",
    "Power",
    "Defense",
    "Health",
    "Intelligence",
    "Set",
]

# Guess cards
card_guess = guess_card(cards)
while card_guess != random_card:
    # Guess was incorrect
    print("Incorrect guess")

    # Reveal card info
    name_symbol = match_name(card_guess["name"], random_card["name"])
    color_symbol = match_color(card_guess["color"], random_card["color"])
    pitch_symbol = match_pitch(card_guess["pitch"], random_card["pitch"])
    print(card_guess["pitch"] + " : " + random_card["pitch"])
    print(str(type(card_guess["pitch"])) + " : " + str(type(random_card["pitch"])))
    cost_symbol = match_cost(card_guess["cost"], random_card["cost"])
    print(card_guess["cost"] + " : " + random_card["cost"])
    print(str(type(card_guess["pitch"])) + " : " + str(type(random_card["pitch"])))
    power_symbol = match_power(card_guess["power"], random_card["power"])
    defense_symbol = match_defense(card_guess["defense"], random_card["defense"])
    health_symbol = match_health(card_guess["health"], random_card["health"])
    intelligence_symbol = match_intelligence(
        card_guess["intelligence"], random_card["intelligence"]
    )
    set_id_symbol = match_set_id(card_guess["set_id"], random_card["set_id"])
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
            set_id_symbol,
        ]
    )
    print(table)

    # Obtain new card guess
    card_guess = guess_card(cards)

    # Check if guess is correct
    if card_guess == random_card:
        print("**Card correctly guessed**")


# card_name = ""
# card_color = ""
# while not match_card(lookup_card(card_name, card_color, cards), random_card):
#     print("Cards don't match")
#     card_name = input()
#     card_color = input()

#     while not card_exists(card_name, card_color, cards):
#         print("No such card exists")
#         card_name = input()
#         card_color = input()

# print("Cards match")
