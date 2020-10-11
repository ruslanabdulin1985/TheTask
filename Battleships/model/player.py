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
        self.recieve = set() # recieved shots
        self.ships = [] # list of ships
        self.score = 0
        self.score_multiplexor = 1;

    def add_score(self):
        """
        ads score to the player's score

        score calculates based on multiplexor. The greater multiplexor the more score is added
        """
        self.score = self.score + 10*self.score_multiplexor
        self.score_multiplexor += 1

    def has_more_alive_ships(self) ->bool:
        """
        checks if the player has alive ships.

        This function is required to find whether the Player lost the game or not

        :return: True if at least one ship left alive. Otherwise False
        """
        for ship in self.ships:
            if not ship.is_dead():
                return True

        return False

    def add_dict_of_ships(self, dict_of_ships):
        """
            turns a dictionary into a set of ships and adds them to the ship

            ship must be in format {"s_type":"2", "set_of_coordinates" : [{"x":"a", "y":1},{"x":"a", "y":2}]}
        """
        for ship in dict_of_ships:
            set_of_coordinates = []
            for coordinates in ship['set_of_coordinates']:
                new_coordinates = Coordinates(coordinates['x'], coordinates['y'])
                set_of_coordinates.append(new_coordinates)

            new_ship = Ship(int(ship['s_type']), set_of_coordinates)
            self.ships.append(new_ship)

    def get_alive_ships(self):
        alive_ships = []
        for ship in self.ships:
            if ship is not ship.is_dead():
                alive_ships.append(ship)
        return alive_ships

    def is_received_duplicates(self, coordinates):
        for old_received_coordinates in self.recieve:  # check if coordinates duplicate
            if coordinates.match(old_received_coordinates):
                return True
        return False
