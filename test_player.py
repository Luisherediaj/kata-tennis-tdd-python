import unittest
from player import Player




class TestPlayer (unittest.TestCase):
    def test_initialScore(self):
        player = Player()
        self.assertEqual("0", player.getScore())
    
    def test_firstPoint(self):
        player = Player()
        player.winPoint()
        self.assertEqual("15", player.getScore())

    def test_secondPoint(self):
        player = Player(1)
        player.winPoint()
        self.assertEqual("30", player.getScore())
    def test_thirdPoint(self):
        player = Player(2)
        player.winPoint()
        self.assertEqual("40", player.getScore())

    
    def test_playerWins(self):
        player1  = Player(3)
        player2 = Player()
        player1.winPoint(player2)
        self.assertEqual("Winner", player1.getScore())

    def test_playerScoresOnDeuce(self):
        player1 = Player(3)
        player2 = Player(3)
        player1.winPoint(player2)
        self.assertEquals("Advantage", player1.getScore())
    
    def test_playerScoresAndOtherPlayerLosesAdvantage(self):
        player1 = Player(4)
        player2 = Player(3)
        player2.winPoint(player1)
        self.assertEqual("40", player1.getScore())
        self.assertEqual("40", player1.getScore())