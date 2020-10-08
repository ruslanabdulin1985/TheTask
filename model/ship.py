"""
Contains class Ship

imports Coordinates to attach them to a Ship
"""

from model.coordinates import Coordinates

class Ship:
    """
    Represents a ship

    This class represents a ship in the game. Each ship has a set of coordinates describing her location on the board
    A ship also has a type representing how many cells the ship takes on the board.
    """
    def __init__(self, s_type: int, set_of_coordinates: list):
        """
        Constructor

        :param s_type: Ship type in range 1-4. this number is the number of cells the ship is taken
        :param set_of_coordinates: A list of cell's coordinates taken by the ship
        """
        self.s_type = s_type
        self.set_of_coordinates = set_of_coordinates
        self.is_alive = True

    def is_dead(self, set_of_hits:list)->bool:
        """
        mehtod to check whether the ship has at least one cell not hit by enemies

        :param set_of_hits: set of hits received by the player
        :return: True if at least one cell is alive. Otherwise False
        """
        counter = 0;
        for s_coordinates in self.set_of_coordinates:
            for h_coordinates in set_of_hits:
                if s_coordinates.match(h_coordinates):
                    counter += 1
                    continue

        if counter==self.s_type:
            return False
        else:
            return True

    def calculate_dead_coordinates(self)->list:
        """
        Surrond the dead ship with misses

        When the ship is dead it is automatically surrounded with missed hits on the board. This method calculates
        coordinates of the hits

        :return: set of coordinates of surrounding cells
        """
        to_return = []
        for coordinates in self.set_of_coordinates:
            try:
                to_return.append(Coordinates(coordinates.x, coordinates.next_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.x, coordinates.prev_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.next_x(), coordinates.next_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.next_x(), coordinates.prev_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.next_x(), coordinates.y))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x(), coordinates.next_y()))
            except:

                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x(), coordinates.prev_y()))
            except:

                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x(), coordinates.y))
            except:

                pass # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x(), coordinates.y))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit

        return to_return
