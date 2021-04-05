import unittest
from player import Player




class TestPlayer (unittest.TestCase):
    def test_initialScore(self):
        player = Player ()
        self.assertEqual("0", player.getScoer())