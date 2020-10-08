"""
Main runnable module which represents Controller of MVC pattern

import Model classess
returns View templates
"""


from flask import Flask, render_template
from model.games import Games
from model.game import Game
from model.player import Player
from model.ship import Ship
from model.coordinates import Coordinates

app = Flask(__name__)

#FIXME
p1 = Player("Vasya");
p2 = Player("Kolya");

g = Game(1, p1, p2);

p1.ships.append(Ship(2, [Coordinates('e', 1), Coordinates('f', 1)]))
p1.ships.append(Ship(2, [Coordinates('b', 4), Coordinates('a', 4)]))
p1.ships.append(Ship(4, [Coordinates('j', 7), Coordinates('i', 7), Coordinates('h', 7), Coordinates('g', 7)]))
p1.ships.append(Ship(2, [Coordinates('d', 5), Coordinates('d', 6)]))

p2.ships.append(Ship(2, [Coordinates('a', 1), Coordinates('a', 2)]))
p2.ships.append(Ship(3, [Coordinates('a', 5), Coordinates('a', 6), Coordinates('a', 7)]))
p2.ships.append(Ship(3, [Coordinates('c', 3), Coordinates('c', 2), Coordinates('c', 4)]))
p2.ships.append(Ship(4, [Coordinates('e', 2), Coordinates('e', 3), Coordinates('e', 4), Coordinates('e', 5)]))
# api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setup")
def setup():
    return render_template('setup.html')

@app.route("/setup_player/<number>")
def setup():
    return render_template('setup.html')

@app.route("/board")
def board():
    return render_template('board.html', data={"active_player": g.turn, "passive_player": g.next_player()})


@app.route("/game")
def status():
      return render_template('game.html', data={"active_player": g.turn})

@app.route("/status<coordinates>")
def status_c(coordinates):
    if len(coordinates)==2:
        result = g.fire(g.turn, g.next_player(), Coordinates(coordinates[0], int(coordinates[1])))

    elif len(coordinates) == 3:
        result = g.fire(g.turn, g.next_player(), Coordinates(coordinates[0], int(coordinates[1]+coordinates[2])))

    return render_template('status.html', data={"active_player": g.turn, "passive_player": g.next_player(), "result": result, "e":{'test':'case'}})

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0', ) #ssl_context='adhoc')
