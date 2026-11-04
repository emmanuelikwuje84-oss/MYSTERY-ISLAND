
# main.py

"""
Mystery Island: The Lost Lighthouse

This module handles all terminal interaction.
It communicates with the game engine in game.py.
"""

from game import (
    new_game,
    get_location_info,
    get_available_moves,
    explore_location,
    collect_item,
    move_player,
    restore_beacon,
    show_status,
    show_inventory,
    is_win,
    is_loss,
    location_items
)


# ==================================================
# 1. DISPLAY TITLE
# ==================================================

def show_title():

    print("\n")
    print("=" * 55)
    print("                                                     ")
    print("             MYSTERY ISLAND                         ")
    print("                                                     ")
    print("           THE LOST LIGHTHOUSE                      ")
    print("                                                     ")
    print("=" * 55)

    print("\n         AN ADVENTURE OF SURVIVAL AND DISCOVERY\n")


# ==================================================
# 2. DISPLAY INSTRUCTIONS
# ==================================================

def show_instructions():

    print("\n" + "=" * 55)
    print("                 YOUR MISSION")
    print("=" * 55)

    print("""
A terrible storm has left you stranded on a mysterious
island.

As you regain consciousness on the beach, you notice
an old lighthouse in the distance.

Its beacon has stopped shining.

A rescue boat may be passing somewhere across the ocean,
but without the lighthouse signal, nobody will find you.

You must explore the island, discover useful objects,
overcome obstacles and restore the lighthouse beacon
before your energy runs out.

YOUR OBJECTIVES:

1. Explore the island and discover useful objects.
2. Find the Rope in the Jungle.
3. Find the Lantern in the Cave.
4. Use the Rope to cross the damaged bridge.
5. Reach the Lighthouse.
6. Restore the beacon using the Lantern.

ENERGY RULES:

- You start with 5 energy points.
- Every successful movement costs 1 energy.
- Exploration costs no energy, even when repeated.
- Collecting items costs no energy.
- Checking your inventory costs no energy.
- Checking your status costs no energy.
- Invalid actions cost no energy.
- Failed bridge crossings cost no energy.
- Every successful movement costs energy, even if
  the movement is unnecessary.
- Your adventure ends when energy reaches zero.

IMPORTANT:

- You can explore a location more than once.
- You can only collect each useful item once.
- You can move backwards to previously visited locations.
- You must follow the island's connected movement routes.

GOOD LUCK, EXPLORER!
""")

    print("=" * 55)


# ==================================================
# 3. GET PLAYER NAME
# ==================================================

def get_player_name():

    while True:

        name = input("\nWhat is your name, explorer? ").strip()

        if not name:
            print("Your name cannot be empty.")

        elif len(name) > 30:
            print("Please use a name of 30 characters or fewer.")

        else:
            return name


# ==================================================
# 4. DISPLAY PLAYER INFORMATION
# ==================================================

def display_status(player):

    print("\n" + "-" * 45)
    print("                 PLAYER STATUS")
    print("-" * 45)

    print(show_status(player))

    print("-" * 45)


# ==================================================
# 5. DISPLAY INVENTORY
# ==================================================

def display_inventory(player):

    print("\n" + "-" * 45)
    print("                  INVENTORY")
    print("-" * 45)

    print(show_inventory(player))

    print("-" * 45)


# ==================================================
# 6. DISPLAY MOVEMENT MENU
# ==================================================

def movement_menu(player):

    destinations = get_available_moves(player)

    print("\n" + "-" * 45)
    print("                TRAVEL OPTIONS")
    print("-" * 45)

    print(f"\nYou are currently at: {player['location']}")

    print("\nAvailable destinations:")

    for number, destination in enumerate(destinations, start=1):
        print(f"{number}. {destination}")

    print("0. Return to previous menu")

    choice = input("\nWhere would you like to travel? ").strip()

    if choice == "0":
        print("You decided to stay where you are.")
        return

    if not choice.isdigit():
        print("Invalid input. Please enter a menu number.")
        return

    choice_number = int(choice)

    if choice_number < 1 or choice_number > len(destinations):
        print("That destination is not available.")
        return

    destination = destinations[choice_number - 1]

    print(move_player(player, destination))


# ==================================================
# 7. DISPLAY LOCATION ACTIONS
# ==================================================

def get_location_actions(player):

    current_location = player["location"]

    actions = []

    # Exploration is always available.
    actions.append(("Explore this location", "explore"))

    # Offer collection only when an item has been discovered
    # but has not yet been collected.
    if current_location in location_items:

        item = location_items[current_location]

        if (
            item in player["discovered_items"]
            and item not in player["inventory"]
        ):
            actions.append(("Collect discovered item", "collect"))

    actions.append(("Travel to another location", "move"))

    actions.append(("Check inventory", "inventory"))

    actions.append(("Check player status", "status"))

    actions.append(("View game instructions", "help"))

    if current_location == "Lighthouse":
        actions.append(("Restore lighthouse beacon", "restore"))

    actions.append(("Quit game", "quit"))

    return actions


# ==================================================
# 8. HANDLE PLAYER ACTIONS
# ==================================================

def handle_action(player, action):

    if action == "explore":

        print("\n" + explore_location(player))

    elif action == "collect":

        print("\n" + collect_item(player))

    elif action == "move":

        movement_menu(player)

    elif action == "inventory":

        display_inventory(player)

    elif action == "status":

        display_status(player)

    elif action == "help":

        show_instructions()

    elif action == "restore":

        print(restore_beacon(player))

    elif action == "quit":

        confirm = input(
            "\nAre you sure you want to quit? (yes/no): "
        ).strip().lower()

        if confirm in ("yes", "y"):

            player["outcome"] = "quit"

            print("\nYou have chosen to leave the island.")

        elif confirm in ("no", "n"):

            print("Your adventure continues!")

        else:

            print("Invalid response. Your adventure continues.")


# ==================================================
# 9. MAIN GAME LOOP
# ==================================================

def play_game():

    show_title()

    show_instructions()

    name = get_player_name()

    player = new_game(name)

    print("\n" + "=" * 55)

    print(f"Welcome, {name}!")

    print("Your adventure begins now.")

    print("\nStarting location: Beach")
    print("Starting energy: 5")

    print("=" * 55)

    # The game continues while the player is playing.
    while player["outcome"] == "playing":

        print("\n\n" + "#" * 55)

        print(f"EXPLORER: {player['name'].upper()}")

        print(f"LOCATION: {player['location'].upper()}")

        print(f"ENERGY: {player['energy']}/5")

        print("#" * 55)

        print("\n" + get_location_info(player))

        actions = get_location_actions(player)

        print("\n" + "-" * 45)
        print("              WHAT WOULD YOU LIKE TO DO?")
        print("-" * 45)

        for number, action in enumerate(actions, start=1):
            print(f"{number}. {action[0]}")

        choice = input("\nEnter your choice: ").strip()

        if not choice.isdigit():

            print(
                "\nInvalid input. Please enter a number "
                "from the menu."
            )

            continue

        choice_number = int(choice)

        if choice_number < 1 or choice_number > len(actions):

            print(
                "\nThat option does not exist. "
                "Please choose an available option."
            )

            continue

        selected_action = actions[choice_number - 1][1]

        handle_action(player, selected_action)

    # Display the ending.
    if is_win(player):

        print("\n" + "=" * 55)
        print("              ADVENTURE COMPLETED!")
        print("=" * 55)

        print(f"\nWell done, {player['name']}!")

        print(
            f"You finished with {player['energy']} "
            "energy remaining."
        )

    elif is_loss(player):

        print("\n" + "=" * 55)
        print("                 GAME OVER")
        print("=" * 55)

        print(f"\nSorry, {player['name']}.")

        print(
            "You ran out of energy before completing "
            "your mission."
        )

        print("The lighthouse remains dark...")

    elif player["outcome"] == "quit":

        print("\n" + "=" * 55)
        print("               ADVENTURE PAUSED")
        print("=" * 55)

        print(
            f"\nThank you for exploring, {player['name']}."
        )


# ==================================================
# 10. REPLAY
# ==================================================

def main():

    while True:

        play_game()

        print("\nWould you like to start a new adventure?")

        choice = input(
            "Enter yes or no: "
        ).strip().lower()

        if choice in ("yes", "y"):

            print("\nStarting a new adventure...")

        elif choice in ("no", "n"):

            print("\nThank you for playing!")

            print("Until your next adventure, explorer!")

            break

        else:

            print(
                "\nInvalid response. "
                "The game will now close."
            )

            break


# ==================================================
# 11. PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":

    try:

        main()

    except (KeyboardInterrupt, EOFError):

        print("\n\nGame interrupted. Thank you for playing!")
