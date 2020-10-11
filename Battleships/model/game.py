"""
Module contains class Game

The module imports two Classes of this model: Player to represent players and Coordinates to let players exchange
coordinates
"""

from model.player import Player
from model.coordinates import Coordinates

# FIXME
from model.ship import Ship


class Game:
    """
    Game class represents a game as a set of interactions in between players

    Game is the main class which is responsible for interactions within the game.
    """
    def __init__(self, id: int, player1: Player, player2: Player):
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

    def fire(self, actor: Player, target: Player, coordinates: Coordinates) -> bool:
        """
        Main method of the Game class. Checks if one player hit another

        This method is responsible for handle a situation when one player tries to hit a ship of another,
        the situation is basically main mechanic of the game so the method is crucial

        :param actor: the player who fires
        :param target: the player who receive the fire
        :param coordinates: target coordinates
        :return: True or False depending if the coordinates has a ship on target player's board
        """
        target.recieve.add(coordinates)
        for ship in target.ships: # for each ship
            for s_coordinates in ship.set_of_coordinates:  # for each coordinate
                if s_coordinates.match(coordinates): # if matches to the hit
                    ship.is_alive=not ship.is_dead(target.recieve)  # if hit we need to check if the ship is still allive or not
                    if not ship.is_alive:
                        for d_coordinates in ship.calculate_dead_coordinates(): # if dead mark surround it with hits
                            target.recieve.add(d_coordinates)

                    self.turn.add_score()
                    return True

        self.turn.score_multiplexor = 1;
        self.turn = self.next_player()
        return False



    def next_player(self) ->Player:
        """
        Whose turn is next

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


