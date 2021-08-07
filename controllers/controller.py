from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('base.html', title="Rock Paper Scissors")

@app.route('/<choice1>/<choice2>')
def play_game():
    player1 = Player("player1", "choice1")
    player2 = Player("player2", "choice2")
    Game.get_winner(player1, player2)
    return render_template('index.html', title="game")

    # return game.get_winner(game.player1.choice, game.player2.choice)
#return a string
