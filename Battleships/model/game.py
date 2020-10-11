"""
Module contains class Game

The module imports two Classes of this model: Player to represent players and Coordinates to let players exchange
coordinates
"""

from model.rules import Rules
from model.player import Player
from model.coordinates import Coordinates

# FIXME
from model.ship import Ship


class Game:
    """
    Game class represents a game as a set of interactions in between players

    Game is the main class which is responsible for interactions within the game.
    """
    def __init__(self, id: int, player1: Player, player2: Player, rules:Rules):
        """
        Construnctor of the class

        :param id: each game is supposed to have a unique ID
        :param player1:
        :param player2:
        """
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.turn = player1
        self.rules = rules

    def fire(self, coordinates: Coordinates) -> bool:
        """
        Main method of the Game class. Checks if one player hit another

        This method is responsible for handle a situation when one player tries to hit a ship of another,
        the situation is basically main mechanic of the game so the method is crucial

        :param coordinates: target coordinates
        :return: True or False depending if the coordinates has a ship on target player's board
        """
        if self.next_player().is_received_duplicates(coordinates):
            self.turn = self.next_player()
            self.turn.score_multiplexor = 1
            return False  # prevent duplicates

        else:
            self.next_player().recieve.add(coordinates)

        for ship in  self.next_player().get_alive_ships(): # for each  alive ship
            if ship.is_hit(coordinates):
                ship.hit_points -= 1
                self.turn.add_score()

                if ship.is_dead():
                    for coordinates in ship.calculate_dead_coordinates():
                        self.next_player().recieve.add(coordinates)

                return True

        self.turn.score_multiplexor = 1
        self.turn = self.next_player()
        return False


    def is_game_over(self):
        """
        :return: True if at least one player has no ships left, otherwise False
        """
        if not self.player1.has_more_alive_ships() or not self.player2.has_more_alive_ships():
            return True
        return False


    def next_player(self) ->Player:
        """
        Who's turn is next

        :return: Player who will be making move next
        """
        if self.turn == self.player1:
            return self.player2
        else:
            return self.player1


    def add_player(self,player_num:str, name:str, list_of_ships:list):
        player = Player(name)

        if player_num == '1':
            self.player1 = player
            self.turn = player

        if player_num == '2':
            self.player2 = player


