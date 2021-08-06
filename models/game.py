from models.player import Player

class Game():
    def __init__(self, player):
        self.player = player
    
    player1 = Player("John", "rock")
    player2 = Player("Sam", "paper")

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
        

        
            
