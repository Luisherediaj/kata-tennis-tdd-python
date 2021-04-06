import unittest
from player import Player




class TestPlayer (unittest.TestCase):
    def test_initialScore(self):
        player = Player ()
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