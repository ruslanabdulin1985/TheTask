"""
Main runnable module which represents Controller of MVC pattern

import Model classess
returns View templates or JSON data
"""


from flask import Flask, request, render_template

from model.game import Game
from model.highscore import HighScore
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

highscore = HighScore()
game = new_game()

@app.route("/")
def index():
    """

    Start Page
    """
    global game
    game = new_game()
    return render_template('index.html')

@app.route("/setup")
def setup():
    """
    Initial setup of the game - e.g HUMAN or AI, set of rules, etc
    """
    return render_template('setup.html')

@app.route("/setup_player/<number>")
def setup_player(number):
    """
    Initial setup of the a player

    Set of ships and a name to chose. Also ship alocation happens on this page
    """
    return render_template('setup_player.html', data={"player": number, 'rules':game.rules})

@app.route("/board")
def board():
    """
    Boards of a player to be shown

    """
    return render_template('board.html', data={"active_player": game.turn, "passive_player": game.next_player()})


@app.route("/game")
def start():
    """
    Start the game

    """
    game.turn = game.player1
    return render_template('game.html', data={"active_player": game.turn})


@app.route("/high_scores")
def high_scores():
    """
    Page for highscores
    """
    return render_template('high_scores.html', data=highscore)


@app.route("/about")
def about():
    """
    about page
    """
    return render_template('about.html', data=highscore)


@app.route("/save_setup/<player_num>", methods=['POST'])
def save_setup(player_num):
    """
    Save setup to the model

    Recieves setup to start with as JSON object and sends it directly to the model

    """
    content = request.json

    player = Player(content['player']['name'])
    dict_of_ships = content['list_of_ships']
    player.add_dict_of_ships(dict_of_ships)

    if player_num == "1":
        game.player1 = player

    if player_num == "2":
        game.player2 = player

    # return {"name": "OK"}  causes bug on some computers
    return 'text'



@app.route("/status<coordinates>")
def status_c(coordinates):
    """
     Result of a guessing action

    this method process coordinates to check whether one player hit or missed a ship of another
     """
    if len(coordinates)==2:
        result = game.fire(Coordinates(coordinates[0], int(coordinates[1])))

    elif len(coordinates) == 3:
        result = game.fire(Coordinates(coordinates[0], int(coordinates[1]+coordinates[2])))
    # print("game_over_check")
    if game.is_game_over():
        # print("game_over")
        highscore.add_player(game.turn)
        highscore.add_player(game.next_player())
    return render_template('status.html', data={"active_player": game.turn, "passive_player": game.next_player(), "result": result})

if __name__ == '__main__':
    app.run(debug=False, host= '127.0.0.1')
