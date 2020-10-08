class Player:
    def __init__(self, name: str):
        self.name = name
        # self.send = set() # sent shots
        self.recieve = set() # recieved shots
        self.ships = [] # list of ships