from model.player import Player
from model.coordinates import Coordinates


class Game:
    def __init__(self, id: int, player1: Player, player2: Player):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def fire(self, actor: Player, target: Player, coordinates: Coordinates) -> bool:
        actor.send.append(coordinates)
        target.recieve.append(coordinates)
        self.turn = self.next_player()
        for ship in target.ships:
            for s_coordinates in ship.set_of_coordinates:
                if s_coordinates.match(coordinates):
                    return True

        return False

    def next_player(self) ->Player:
        if self.turn == self.player1:
            return self.player2
        else:
            return self.player1