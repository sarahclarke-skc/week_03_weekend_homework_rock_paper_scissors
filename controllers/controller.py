from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('base.html', title="Rock Paper Scissors")

    # return game.get_winner(game.player1.choice, game.player2.choice)
#return a string
