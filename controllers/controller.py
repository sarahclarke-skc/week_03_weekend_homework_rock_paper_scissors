from flask import render_template, request
from app import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('base.html', title="Rock Paper Scissors")

#method to be POST
@app.route('/play') 
def play():
    # player1 = taken from form imput
    # player2 = computer
    return render_template('play.html', title="Play Rock Paper Scissors")

@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):
    player1 = Player("player 1", choice1)
    player2 = Player("player 2", choice2)
    game = Game(player1,player2)
    winner = game.get_winner(player1, player2)
    return render_template('result.html', title="Results", winner = winner)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Welcome')



    # return game.get_winner(game.player1.choice, game.player2.choice)
#return a string
