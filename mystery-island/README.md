
# Mystery Island: The Lost Lighthouse

A terminal-based Python adventure game about survival, exploration, and decision-making.

## 1. Project Overview

The player survives a terrible storm and becomes stranded on a mysterious island. To attract a rescue boat, the player must find useful items, overcome obstacles, and restore the Lighthouse beacon.

## 2. Game Objective

The player must:
1. Find and collect the Rope in the Jungle.
2. Find and collect the Lantern in the Cave.
3. Use the Rope to cross the damaged bridge.
4. Reach the Lighthouse.
5. Use the Lantern to restore the beacon.

## 3. Game Locations

The island has five connected locations:

- Beach – Starting location.
- Jungle – Contains the Rope.
- Cave – Contains the Lantern.
- Old Bridge – Requires the Rope to cross.
- Lighthouse – Final destination.

The player can move backwards but cannot skip connected locations.

## 4. Energy Rules

The player starts with **5 energy points**.

| Action | Energy Cost |
|---|---:|
| Successful movement | 1 |
| Exploration | 0 |
| Repeated exploration | 0 |
| Collecting items | 0 |
| Checking inventory/status | 0 |
| Invalid actions | 0 |
| Failed bridge crossing | 0 |

Every successful movement costs 1 energy, even if unnecessary. The player loses when energy reaches zero.

## 5. Item Rules

- Items must be discovered through exploration before collection.
- Each item can only be collected once.
- Collected items remain in the inventory.
- Items are not consumed when used.

## 6. Winning and Losing

**Win:** Restore the Lighthouse beacon using the Lantern after successfully crossing the bridge with the Rope.

**Lose:** Energy reaches zero before completing the mission.

The player can also quit and start a new adventure.

## 7. Project Structure

```text
mystery-island/
├── main.py
├── game.py
├── tests/
│   ├── __init__.py
│   └── test_game.py
├── README.md
└── .gitignore
```

- `main.py` – Handles menus and player interaction.
- `game.py` – Contains game rules and logic.
- `tests/test_game.py` – Contains automated tests.
- `.gitignore` – Excludes unnecessary files.

## 8. Requirements

- Python 3
- Python standard library only.
- No external packages required.

## 9. How to Run

Activate the virtual environment if you have one:

```bash
source .venv/bin/activate
```

Run the game:

```bash
python main.py
```

Run automated tests:

```bash
python -m unittest discover -s tests -v
```

## 10. Concepts Demonstrated

- Variables and data types
- Lists and dictionaries
- Conditions and loops
- Functions and modules
- Input validation
- State management
- Error handling
- Automated testing

---

**Project:** Mystery Island: The Lost Lighthouse  
**Language:** Python
