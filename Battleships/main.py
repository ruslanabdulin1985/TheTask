"""
Main runnable module which represents Controller of MVC pattern

import Model classess
returns View templates
"""


from flask import Flask, request, render_template

from model.game import Game
from model.app import App
from model.player import Player
from model.ship import Ship
from model.coordinates import Coordinates
from model.rules import Rules


app = Flask(__name__)

def new_game():
    player1 = Player("Player 1");
    player2 = Player("Player 2");
    rules = Rules(mode='standard', opponent='human')
    new_g = Game(1, player1, player2, rules);
    return new_g

game = new_game()

@app.route("/")
def index():
    global game
    game = new_game()
    return render_template('index.html')

@app.route("/setup")
def setup():
    return render_template('setup.html')

@app.route("/setup_player/<number>")
def setup_player(number):
    return render_template('setup_player.html', data={"player": number, 'rules':game.rules})

@app.route("/board")
def board():
    return render_template('board.html', data={"active_player": game.turn, "passive_player": game.next_player()})


@app.route("/game")
def status():
    return render_template('game.html', data={"active_player": game.turn})


@app.route("/save_setup/<player_num>", methods=['POST'])
def save_setup(player_num):
    content = request.json

    player = Player(content['player']['name'])
    dict_of_ships = content['list_of_ships']
    player.add_dict_of_ships(dict_of_ships)

    if player_num == "1":
        game.player1 = player
    if player_num == "2":
        game.player2 = player

    return {"name": "OK"}



@app.route("/status<coordinates>")
def status_c(coordinates):
    if len(coordinates)==2:
        result = game.fire(Coordinates(coordinates[0], int(coordinates[1])))

    elif len(coordinates) == 3:
        result = game.fire(Coordinates(coordinates[0], int(coordinates[1]+coordinates[2])))

    return render_template('status.html', data={"active_player": game.turn, "passive_player": game.next_player(), "result": result, "e":{'test':'case'}})

if __name__ == '__main__':
    app.run(debug=False, host= '127.0.0.1')
