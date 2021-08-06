from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/<choice1>/<choice2>')
def get_winner():
    pass
#return a string