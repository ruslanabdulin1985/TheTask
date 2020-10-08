import unittest
from model.coordinates import Coordinates

class TestModelClasses(unittest.TestCase):

    def test_coordinates(self):
        c1 = Coordinates('a', 1)
        c2 = Coordinates('a', 1)
        c3 = Coordinates('b', 1)
        c4 = Coordinates('a', 2)
        self.assertTrue(c1.match(c2))
        self.assertFalse(c1.match(c3))
        self.assertFalse(c1.match(c4))
        self.assertRaises(Exception, Coordinates, 'a', 11)
        self.assertRaises(Exception, Coordinates,'y', 7)

if __name__ == '__main__':
    unittest.main()