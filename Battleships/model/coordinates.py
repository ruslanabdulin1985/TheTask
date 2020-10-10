"""
Module contains class coordinates

Class coordinates represent a pair of coordinates of a single cell on a 10x10 board
"""

class Coordinates:
    """
    Represents coordinates of a single cell

     Represents coordinates of a single cell with x and y coordinates where x abs is a top row in range a-j and y abs
     is leftmost columnt 1-10
    """

    def __init__(self, x:str, y:int):
        """
        Constructor of the class coordinates

        :param x: a string of a single letter in range a-b
        :param y: an integer in range [1-10]
        """
        if all([y>0, y<11]) and x in ['a','b','c','d','e','f','g','h','i','j']:
            self.x = x
            self.y = y
        else:
            raise Exception('invalid coordinates values')


    def match(self, coordinates) -> bool:
        """
        check if one object has the same coordinates as another

        :param coordinates:
        :return: True or False
        """
        if coordinates.x == self.x and coordinates.y == self.y:
            return True
        return False

    def next_y(self):
        """
        next y coordinate

        :return: next y value
        """
        if self.y<10:
            return self.y+1
        else:
            return None
            # raise Exception('can not go beyond the limit')

    def prev_y(self):
        """
        perv y coordinate

        :return: prev y value
        """
        if self.y > 1:
            return self.y - 1
        else:
            return None
            # raise Exception('can not go beyond the limit')

    def next_x(self):
        """
        next x coordinate

        :return: next x value
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        index = letters.index(self.x)

        if index < 9:
            return letters[index + 1]
        else:
            return None
            # raise Exception('can not go beyond the limit')

    def prev_x(self):
        """
        prev x coordinate

        :return: prev x value
        """
        letters = ['a','b','c','d','e','f','g','h','i','j']
        index = letters.index(self.x)

        if index > 0 :
            return letters[index-1]
        else:
            return None
            # raise Exception('can not go beyond the limit')

