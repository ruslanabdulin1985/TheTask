from model.coordinates import Coordinates

class Ship:
    def __init__(self, s_type: int, set_of_coordinates: list):
        self.s_type = s_type
        self.set_of_coordinates = set_of_coordinates
        self.is_alive = True

    def is_dead(self, set_of_hits:list)->bool:
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
                to_return.append(Coordinates(coordinates.next_x, coordinates.next_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.next_x, coordinates.prev_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.next_x, coordinates.y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x, coordinates.next_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x, coordinates.next_y()))
            except:
                pass  # don't do anything as coordinates might be wrong because they are beyond the limit
            try:
                to_return.append(Coordinates(coordinates.prev_x, coordinates.y()))
            except:
                pass # don't do anything as coordinates might be wrong because they are beyond the limit

        return to_return
