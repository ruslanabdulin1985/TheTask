from model.coordinates import Coordinates

class Ship:
    def __init__(self, s_type: int, set_of_coordinates: list):
        self.s_type = s_type
        self.set_of_coordinates = set_of_coordinates
        self.is_alive = True;
