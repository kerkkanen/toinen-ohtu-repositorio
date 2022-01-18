from re import S
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_right_team(self):
        list = self.statistics.team("EDM")
        self.assertEqual(len(list), 3)

    def test_top_scorer_right(self):
        list = self.statistics.top_scorers(2)
        st = list[0]
        nd = list[1]
        self.assertTrue(st.points >= nd.points)

    def test_search_works(self):
        self.assertEqual(self.statistics.search("Koivu"), None)
        player = self.statistics.search("Kurri")
        self.assertTrue(player.points, 90)