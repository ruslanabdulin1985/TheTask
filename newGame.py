from model.game import Game
from model.player import Player
from model.ship import Ship
from model.ship import Coordinates

if __name__ == "__main__":
    p1 = Player("Vasya");
    p2 = Player("Kolya");

    g = Game(1, p1, p2);

    p2.ships.append(Ship(2, [Coordinates('a', 1), Coordinates('a', 2)]))

    print(g.fire(p1, p2, Coordinates("a", 2)))
