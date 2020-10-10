
class Rules:
    def __init__(self, mode, opponent):
        self.shipSet = [4,3,3,2,2,2,1,1,1,1];  # each element is a ship. e.g [4,3,3] say that there is 1 of type 4 and 2
                                                # of type 3 in the set
        self.opponent = 'human' # human or computer
