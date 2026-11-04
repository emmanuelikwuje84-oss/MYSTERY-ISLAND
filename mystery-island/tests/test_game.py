
# tests/test_game.py

import unittest

from game import (
    new_game,
    locations,
    STARTING_ENERGY,
    explore_location,
    collect_item,
    move_player,
    restore_beacon,
    is_win,
    is_loss
)


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Emmanuel")

    def test_new_player(self):
        self.assertEqual(self.player["name"], "Emmanuel")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])

    def test_starting_energy(self):
        self.assertEqual(STARTING_ENERGY, 5)

    def test_map_connections(self):
        self.assertEqual(locations["Beach"], ["Jungle"])
        self.assertEqual(locations["Jungle"], ["Beach", "Cave"])
        self.assertEqual(locations["Cave"], ["Jungle", "Old Bridge"])
        self.assertEqual(locations["Old Bridge"], ["Cave", "Lighthouse"])

    def test_exploration_does_not_cost_energy(self):
        explore_location(self.player)
        self.assertEqual(self.player["energy"], 5)

    def test_repeated_exploration_does_not_cost_energy(self):
        self.player["location"] = "Jungle"

        explore_location(self.player)
        explore_location(self.player)

        self.assertEqual(self.player["energy"], 5)

    def test_exploration_discovers_rope(self):
        self.player["location"] = "Jungle"

        explore_location(self.player)

        self.assertIn("Rope", self.player["discovered_items"])

    def test_collect_without_exploring(self):
        self.player["location"] = "Jungle"

        result = collect_item(self.player)

        self.assertNotIn("Rope", self.player["inventory"])
        self.assertIn("explore", result.lower())

    def test_collect_rope(self):
        self.player["location"] = "Jungle"

        explore_location(self.player)
        collect_item(self.player)

        self.assertIn("Rope", self.player["inventory"])
        self.assertEqual(self.player["energy"], 5)

    def test_item_cannot_be_collected_twice(self):
        self.player["location"] = "Jungle"

        explore_location(self.player)
        collect_item(self.player)
        collect_item(self.player)

        self.assertEqual(self.player["inventory"].count("Rope"), 1)

    def test_successful_movement_costs_one_energy(self):
        result = move_player(self.player, "Jungle")

        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)
        self.assertIn("successfully", result.lower())

    def test_unnecessary_successful_movement_still_costs_energy(self):
        move_player(self.player, "Jungle")
        move_player(self.player, "Beach")

        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 3)

    def test_invalid_movement_does_not_cost_energy(self):
        result = move_player(self.player, "Cave")

        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("cannot", result.lower())

    def test_bridge_requires_rope(self):
        self.player["location"] = "Old Bridge"

        result = move_player(self.player, "Lighthouse")

        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("Rope", result)

    def test_bridge_crossing_with_rope(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"].append("Rope")

        move_player(self.player, "Lighthouse")

        self.assertEqual(self.player["location"], "Lighthouse")
        self.assertEqual(self.player["energy"], 4)

    def test_zero_energy_causes_loss(self):
        self.player["energy"] = 1

        move_player(self.player, "Jungle")

        self.assertTrue(is_loss(self.player))
        self.assertEqual(self.player["energy"], 0)

    def test_lantern_required_to_restore_beacon(self):
        self.player["location"] = "Lighthouse"

        result = restore_beacon(self.player)

        self.assertFalse(is_win(self.player))
        self.assertIn("Lantern", result)

    def test_successful_victory(self):
        self.player["location"] = "Lighthouse"
        self.player["inventory"].append("Lantern")

        result = restore_beacon(self.player)

        self.assertTrue(is_win(self.player))
        self.assertIn("won", result.lower())

    def test_exploration_after_game_ends(self):
        self.player["outcome"] = "lost"

        result = explore_location(self.player)

        self.assertIn("ended", result.lower())


if __name__ == "__main__":
    unittest.main()
