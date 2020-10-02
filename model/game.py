from model.player import Player

class Game:
    def __init__(self, id: int):
        self.id = id
        self.player1 = None
        self.player2 = None