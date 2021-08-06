from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/<player.choice>/<player.choice>')
def print_winner(game):
    game.get_winner(game.player1.choice, game.player2.choice)
#return a string