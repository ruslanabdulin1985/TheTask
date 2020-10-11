"""
Module for Highscore class
"""
from model.player import Player

class HighScore:
    """
    Represents high score and list of players
    """
    def __init__(self):
        self.high_score = 0
        self.best_player = None
        self.list_of_playes = []

    def add_player(self, player:Player):
        """
        Adds a player to the list of players and checks if he is the best one. IF so sets
        as the best

        """
        if self.best_player is None:
            self.best_player = player

        if self.best_player.score < player.score:
            self.best_player = player

        self.list_of_playes.append(player)