from pygame import Vector2

import core
from agario.Player import Player


class Map:
    def __init__(self):
        self.maxPlayer=20
        self.maxFood=200
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []
        self.food = []
        self.pieges = []

    def spawn_food(self):
        pass

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()

    def addJoueur(self,p):
        if len(self.joueurs)<self.maxPlayer:
            self.joueurs.append(Player())