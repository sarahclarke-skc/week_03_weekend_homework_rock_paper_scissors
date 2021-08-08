from models.player import Player
import random

class Game():
    def __init__(self, player, player2):
        self.player = player
        self.player2 = player2
        self.choices = ["rock", "paper", "scissors"]
    
    player1 = Player("player 1", "rock")
    player2 = Player("player 2", "paper")

    def get_computer_player(self, computer):
        computer.name = "Computer"
        computer.choice = random.choice(self.choices)


    def play_computer(self):
        pass

    #Needs refactoring to stop repeating the return statement
    def get_winner(self, player1, player2):
        if player1.choice == "rock" and player2.choice == "paper":
            return f"Congratulations {player1.name}, you have won!"
        elif player1.choice == "rock" and player2.choice == "scissors":
            return f"Congratulations {player1.name}, you have won!"
        elif player1.choice == "paper" and player2.choice == "rock":
            return f"Congratulations {player1.name}, you have won!"
        elif player1.choice == "paper" and player2.choice == "rock":
            return f"Congratulations {player2.name}, you have won!"
        elif player1.choice == "scissors" and player2.choice == "rock":
            return f"Congratulations {player2.name}, you have won!"
        elif player1.choice == "rock" and player2.choice == "paper":
            return f"Congratulations {player2.name}, you have won!"
        elif player1.choice == "paper" and player2.choice == "scissors":
            return f"Congratulations {player2.name}, you have won!"
        elif player1.choice == "scissors" and player2.choice == "paper":
            return f"Congratulations {player1.name}, you have won!"
        elif player1.choice == player2.choice:
            return "It's a tie! Play again!"
    
        

        
            
