import json

class Coordinates:
    def __init__(self, x:str, y:int):
            if all([y>0, y<11]) and x in ['a','b','c','d','e','f','g','h','i','j']:
                self.x = x
                self.y = y
            else:
                raise Exception('invalid coordinates values')


    def match(self, coordinates) -> bool:
        if coordinates.x == self.x and coordinates.y == self.y:
            return True
        return False

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)