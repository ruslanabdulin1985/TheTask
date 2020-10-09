"""
Main runnable module which represents Controller of MVC pattern

import Model classess
returns View templates
"""


from flask import Flask, request, render_template
from model.games import Games
from model.game import Game
from model.player import Player
from model.ship import Ship
from model.coordinates import Coordinates

app = Flask(__name__)

p1 = Player("Player 1");
p2 = Player("Player 2");

g = Game(1, p1, p2);



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setup")
def setup():
    return render_template('setup.html')

@app.route("/setup_player/<number>")
def setup_player(number):
    return render_template('setup_player.html', data={"player": number})

@app.route("/board")
def board():
    print(g.player1.name)
    print(g.player2.name)
    return render_template('board.html', data={"active_player": g.turn, "passive_player": g.next_player()})


@app.route("/game")
def status():
    g.turn = g.player1
    return render_template('game.html', data={"active_player": g.turn})


@app.route("/save_setup/<player_num>", methods=['POST'])
def save_setup(player_num):
    content = request.json
    print(content)

    player = Player(content['player']['name'])
    dict_of_ships = content['list_of_ships']
    player.add_dict_of_ships(dict_of_ships)

    if player_num == "1":
        g.player1 = player
    if player_num == "2":
        g.player2 = player

    return {"name": "OK"}



@app.route("/status<coordinates>")
def status_c(coordinates):
    if len(coordinates)==2:
        result = g.fire(g.turn, g.next_player(), Coordinates(coordinates[0], int(coordinates[1])))

    elif len(coordinates) == 3:
        result = g.fire(g.turn, g.next_player(), Coordinates(coordinates[0], int(coordinates[1]+coordinates[2])))

    return render_template('status.html', data={"active_player": g.turn, "passive_player": g.next_player(), "result": result, "e":{'test':'case'}})

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0', ) #ssl_context='adhoc')
