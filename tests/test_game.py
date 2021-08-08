import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", "rock")
        self.player2 = Player("Sam", "paper")

        self.player3 = Player("Peter", "paper")
        self.player4 = Player("Sue", "rock")
    
    def test_get_winner(self):
        self.assertEqual("Congratulations John, you have won!", Game.get_winner(self, self.player1, self.player2))
    
    def test_get_winner2(self):
        self.assertEqual("Congratulations Peter, you have won!", Game.get_winner(self, self.player3, self.player4))
    
    def test_get_winner_return_tie(self):
        self.assertEqual("It's a tie! Play again!", Game.get_winner(self, self.player2, self.player3))

    # def test_get_computer_player(self):
    #     player = Player(None, None)
    #     Game.get_computer_player(self)
    #     self.assertEqual("rock" or "paper" or "scissors", Game.get_computer_player(self, Player.choice))
