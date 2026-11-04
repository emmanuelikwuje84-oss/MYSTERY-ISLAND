
# ==================================================
# MYSTERY ISLAND: THE LOST LIGHTHOUSE
# game.py
#
# This module contains the game's rules and logic.
# ==================================================


# -------------------------------
# 1. GAME SETTINGS
# -------------------------------

STARTING_ENERGY = 5
MOVEMENT_COST = 1


# -------------------------------
# 2. LOCATION MAP
# -------------------------------

locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


# -------------------------------
# 3. LOCATION DESCRIPTIONS
# -------------------------------

location_descriptions = {
    "Beach": (
        "You are on a lonely beach after surviving "
        "a terrible storm."
    ),

    "Jungle": (
        "You enter a thick jungle. Something useful "
        "may be hidden here."
    ),

    "Cave": (
        "You discover a dark cave. It may contain "
        "something important."
    ),

    "Old Bridge": (
        "You arrive at an old damaged bridge leading "
        "to the Lighthouse."
    ),

    "Lighthouse": (
        "You have reached the abandoned Lighthouse."
    )
}


# -------------------------------
# 4. ITEMS
# -------------------------------

location_items = {
    "Jungle": "Rope",
    "Cave": "Lantern"
}


# -------------------------------
# 5. CREATE A NEW PLAYER
# -------------------------------

def new_game(name):

    return {
        "name": name,
        "location": "Beach",
        "energy": STARTING_ENERGY,
        "inventory": [],
        "discovered_items": [],
        "outcome": "playing"
    }


# -------------------------------
# 6. SPEND ENERGY
# -------------------------------

def spend_energy(player, amount):

    if player["outcome"] != "playing":
        return False

    if player["energy"] < amount:
        return False

    player["energy"] -= amount

    if player["energy"] <= 0:

        player["energy"] = 0
        player["outcome"] = "lost"

        return False

    return True


# -------------------------------
# 7. GET LOCATION INFORMATION
# -------------------------------

def get_location_info(player):

    location = player["location"]

    return location_descriptions[location]


# -------------------------------
# 8. GET AVAILABLE MOVES
# -------------------------------

def get_available_moves(player):

    current_location = player["location"]

    return locations[current_location]


# -------------------------------
# 9. EXPLORE LOCATION
# -------------------------------

def explore_location(player):

    if player["outcome"] != "playing":
        return "The game has already ended."

    location = player["location"]

    print(f"\nYou explore the {location}.")

    if location in location_items:

        item = location_items[location]

        if item not in player["discovered_items"]:

            player["discovered_items"].append(item)

            return (
                f"You discovered a {item}! "
                "You can now collect it."
            )

        return f"You have already discovered the {item} here."

    return "You find nothing useful here."


# -------------------------------
# 10. COLLECT ITEM
# -------------------------------

def collect_item(player):

    if player["outcome"] != "playing":
        return "The game has already ended."

    location = player["location"]

    if location not in location_items:
        return "There is no useful item to collect here."

    item = location_items[location]

    if item not in player["discovered_items"]:

        return (
            "You must explore this location "
            "before collecting the item."
        )

    if item in player["inventory"]:

        return f"You already have the {item}."

    player["inventory"].append(item)

    return f"You collected the {item}!"


# -------------------------------
# 11. MOVE PLAYER
# -------------------------------

def move_player(player, destination):

    if player["outcome"] != "playing":
        return "The game has already ended."

    current_location = player["location"]

    # Check whether the destination is connected.
    if destination not in locations[current_location]:

        return "You cannot move to that location from here."

    # Rope is required to cross the damaged bridge.
    if (
        current_location == "Old Bridge"
        and destination == "Lighthouse"
        and "Rope" not in player["inventory"]
    ):

        return "You need the Rope to cross the damaged bridge."

    # Only successful movement costs energy.
    if not spend_energy(player, MOVEMENT_COST):

        return "You have run out of energy. Game over!"

    player["location"] = destination

    return f"You successfully moved to {destination}."


# -------------------------------
# 12. RESTORE LIGHTHOUSE BEACON
# -------------------------------

def restore_beacon(player):

    if player["outcome"] != "playing":
        return "The game has already ended."

    if player["location"] != "Lighthouse":

        return "You must reach the Lighthouse first."

    if "Lantern" not in player["inventory"]:

        return "You need the Lantern to restore the Lighthouse beacon."

    player["outcome"] = "won"

    return (
        "You restored the Lighthouse beacon! "
        "You have won the game!"
    )


# -------------------------------
# 13. SHOW PLAYER STATUS
# -------------------------------

def show_status(player):

    return (
        f"Explorer: {player['name']}\n"
        f"Current location: {player['location']}\n"
        f"Energy remaining: "
        f"{player['energy']}/{STARTING_ENERGY}\n"
        f"Game outcome: {player['outcome']}"
    )


# -------------------------------
# 14. SHOW PLAYER INVENTORY
# -------------------------------

def show_inventory(player):

    inventory = player["inventory"]

    if not inventory:

        return "Your inventory is empty."

    items = "\n".join(
        f"- {item}" for item in inventory
    )

    return f"Collected items:\n{items}"


# -------------------------------
# 15. CHECK GAME RESULT
# -------------------------------

def is_win(player):

    return player["outcome"] == "won"


def is_loss(player):

    return player["outcome"] == "lost"
