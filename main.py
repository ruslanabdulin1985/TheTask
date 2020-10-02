import time
from threading import Thread
from threading import main_thread

from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import request
from controller.games import Games


app = Flask(__name__)

set_of_games = Games()

# api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setup")
def setup():
    return render_template('setup.html')

@app.route("/game")
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0', ) #ssl_context='adhoc')
