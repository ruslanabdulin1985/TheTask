from model.player import Player
from model.coordinates import Coordinates


class Game:
    def __init__(self, id: int, player1: Player, player2: Player):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def fire(self, actor: Player, target: Player, coordinates: Coordinates) -> bool:
        # actor.send.add(coordinates)
        target.recieve.add(coordinates)
        # self.turn = self.next_player()
        for ship in target.ships:
            for s_coordinates in ship.set_of_coordinates:
                if s_coordinates.match(coordinates):
                    ship.is_alive=ship.is_dead(target.recieve)  # if hit we need to check i the ship is still allive or not
                    if not ship.is_alive:
                        for d_coordinates in ship.calculate_dead_coordinates(): # if not mark it with hits
                            target.recieve.add(d_coordinates)
                            print(d_coordinates.x, d_coordinates.y)
                            # actor.send.add(d_coordinates)

                    return True

        self.turn = self.next_player()
        return False



    def next_player(self) ->Player:
        if self.turn == self.player1:
            return self.player2
        else:
            return self.player1