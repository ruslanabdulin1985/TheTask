class Coordinates:
    def __init__(self, y:str, x:int):
            if all([x>0, x<9]) and y in ['a','b','c','d','e','f','g','h']:
                self.x = x
                self.y = y
            else:
                raise Exception('invalid coordinates values')


    def match(self, coordinates) -> bool:
        if coordinates.x == self.x and coordinates.y == self.y:
            return True
        return False
