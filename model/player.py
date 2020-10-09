"""
module contains class Player

imports model classes
"""
from model.ship import Ship
from model.coordinates import Coordinates

class Player:
    """
    Player represents a human or AI playing the game

    Player class represents an actor of the game. Player has a name, a score and a set of ships
    """
    def __init__(self, name: str):
        """
        constructor

        :param name: each player must have a name
        """
        self.name = name
        # self.send = set() # sent shots
        self.recieve = set() # recieved shots
        self.ships = [] # list of ships

    def has_more_alive_ships(self) ->bool:
        """
        checks if the player has alive ships.

        This function is required to find whether the Player lost the game or not

        :return: True if at least one ship left alive. Otherwise False
        """
        for ship in self.ships:
            if ship.is_alive:
                return True

        return False

    def add_dict_of_ships(self, dict_of_ships):
        print(dict_of_ships)

        for ship in dict_of_ships:
            new_ship = Ship(ship['s_type'], [])
            for coordinates in ship['set_of_coordinates']:
                new_coordinates = Coordinates(coordinates['x'], coordinates['y'])
                new_ship.set_of_coordinates.append(new_coordinates)
            self.ships.append(new_ship)
            print(self.ships)