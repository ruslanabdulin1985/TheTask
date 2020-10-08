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

    def next_y(self):
        if self.y<10:
            return self.y+1
        else:
            raise Exception('can not go beyond the limit')

    def prev_y(self):
        if self.y > 1:
            return self.y - 1
        else:
            raise Exception('can not go beyond the limit')

    def next_x(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        index = letters.index(self.x)

        if index < 9:
            return letters[index + 1]
        else:
            raise Exception('can not go beyond the limit')

    def prev_x(self):
        letters = ['a','b','c','d','e','f','g','h','i','j']
        index = letters.index(self.x)

        if index > 0 :
            return letters[index-1]
        else:
            raise Exception('can not go beyond the limit')

