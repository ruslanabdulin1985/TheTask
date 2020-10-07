class Player:
    def __init__(self, name: str):
        self.name = name
        self.send = [] # sent shots
        self.recieve = [] # recieved shots
        self.ships = [] # list of ships