import unittest
from unittest.mock import patch, Mock

from model.coordinates import Coordinates
from model.ship import Ship
from model.player import Player
from model.game import Game

class TestModelClasses(unittest.TestCase):

    @patch('model.ship.Ship')
    def test_is_dead(self, MockShip):
        ship = MockShip()
        ship.is_dead.return_value = False;
        result = ship.is_dead()

        self.assertEqual(result, False)

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
        self.assertEqual('b', c1.next_x())
        self.assertEqual(2, c1.next_y())
        self.assertEqual('a', c3.prev_x())
        self.assertEqual(1, c4.prev_y())
    #


    def test_ship_is_dead(self, ):
        coordinates1 = Coordinates("a",3)
        coordinates2 = Coordinates("a", 4)
        coordinates3 = Coordinates("a", 2)

        coordinates4 = Coordinates("a", 3)
        coordinates5 = Coordinates("a", 4)
        coordinates6 = Coordinates("a", 2)
        ship = Ship(3, [coordinates1, coordinates2, coordinates3])

        self.assertEqual(True, ship.is_dead([coordinates4, coordinates5, coordinates6]))
        self.assertEqual(False, ship.is_dead([coordinates4, coordinates5, ]), )

    def test_ship_dead_coordinates(self, ):
        ship = Ship(1, [Coordinates("b",2)])

        actual = ship.calculate_dead_coordinates()
        expected = [Coordinates("b",1), Coordinates("b",3), Coordinates("a",1), Coordinates("a",3), Coordinates("c",1),
                    Coordinates("c",3), Coordinates("a",2), Coordinates("c",2)]

        for i in range(len(expected)):
            expected[i].x = actual[i].x

        ship = Ship(2, [Coordinates("b", 2), Coordinates("b", 1)])
        actual = ship.calculate_dead_coordinates()
        expected = [Coordinates("b", 3), Coordinates("a", 1), Coordinates("a", 3),
                    Coordinates("c", 1),
                    Coordinates("c", 3), Coordinates("a", 2), Coordinates("c", 2)]

        for i in range(len(expected)):
            expected[i].x = actual[i].x

    @patch('model.ship.Ship')
    def test_player_more_allive_ships(self, MockShip):
        ship = MockShip()
        ship.is_alive = False
        player = Player('p')
        player.ships.append(ship)

        expected = False
        actual = player.has_more_alive_ships()
        self.assertEqual(expected, actual)

        ship.is_alive = True
        expected = True
        actual = player.has_more_alive_ships()
        self.assertEqual(expected, actual)


    def test_player_add_dict_of_ships(self):

        player = Player('p')
        player.add_dict_of_ships([{"s_type":"2", "set_of_coordinates" : [{"x":"a", "y":1},{"x":"a", "y":2}]}])

        expected = "a"
        actual = player.ships[0].set_of_coordinates[0].x
        self.assertEqual(expected, actual)

        expected = 1
        actual = player.ships[0].set_of_coordinates[0].y
        self.assertEqual(expected, actual)

        expected = "a"
        actual = player.ships[0].set_of_coordinates[1].x
        self.assertEqual(expected, actual)

        expected = 2
        actual = player.ships[0].set_of_coordinates[1].y
        self.assertEqual(expected, actual)

    def test_game_next_player(self):
        p1 = Player('p1')
        p2 = Player('p2')

        g = Game(1, p1, p2)

        expected = p2
        actual = g.next_player()
        self.assertEqual(expected, actual)

    @patch('model.ship.Ship')
    def test_game_fire(self, MockShip):
        ship = MockShip()
        ship.is_alive = True
        ship.set_of_coordinates= [Coordinates('a', 1), Coordinates('a', 2)]


        player1 = Player('p1')

        player2 = Player('p2')
        player2.ships.append(ship)

        g = Game(1, player1, player2)

        expected = True
        actual = g.fire(player1,player2,Coordinates('a', 1))
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()