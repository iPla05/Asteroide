import random
import core
from pygame import Vector2

class Player:
    def __init__(self):
        self.bot=True
        self.name="OUIOUIOUI"
        self.uuid=random.randint(10000000,9999999999)
        self.masse=15
        self.vMax=5
        self.accMax=2
        self.position = Vector2(random.randint(50,950),random.randint(50,750))
        self.vitesse = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def deplacement(self):
        pass

    def grandir(self):
        pass

    def evaportaion(self):
        pass

    def show(self):
        core.Draw.circle(self.couleur,self.position,self.masse)