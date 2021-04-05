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