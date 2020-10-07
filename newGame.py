from model.game import Game
from model.player import Player


if __name__ == "__main__":
    p1 = Player();
    p2 = Player();

    g = Game(1, p1, p2);
