import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", "rock")
        self.player2 = Player("Sam", "paper")

        self.player3 = Player("Peter", "paper")
        self.player4 = Player("Sue", "rock")

        # game1 = Game("John")
    
    def test_get_winner(self):
        self.assertEqual("Congratulations John, you have won!", Game.get_winner(self, self.player1, self.player2))
    
    def test_get_winner2(self):
        self.assertEqual("Congratulations Peter, you have won!", Game.get_winner(self, self.player3, self.player4))
    
    def test_get_winner_return_none(self):
        self.assertEqual(None, Game.get_winner(self, self.player2, self.player3))
