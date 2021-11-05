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
        self.statistics = Statistics(PlayerReaderStub())

    #def test_konstruktori_luo_stub_listan(self):
     #   self.assertAlmostEqual(len(self.statistics), 5)

    def test_search_finds_player(self):
        player1 = self.statistics.search("Semenko")
        #print(player1)

        self.assertAlmostEqual(str(player1), "Semenko EDM 4 + 12 = 16")

    def test_search_finds_no_player(self):
        player = self.statistics.search("Rantanen")

        self.assertAlmostEqual(player, None)

    def test_search_team_players(self):
        team_players = self.statistics.team("EDM")

        self.assertAlmostEqual(len(team_players), 3)
  
    def test_search_team_players(self):
        team_players = self.statistics.team("EDM")

        self.assertAlmostEqual(len(team_players), 3)

    def test_top_scorer_correct(self):
        top_scorer = self.statistics.top_scorers(5)[0]
        #print(top_scorer)
        self.assertAlmostEqual(str(top_scorer), "Gretzky EDM 35 + 89 = 124")
  
    def test_number_of_top_scorers_correct(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertAlmostEqual(len(top_scorers), 3)
  
