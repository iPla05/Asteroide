import core
from JeuxAsteroide import etat
from JeuxAsteroide.etat import Etat


def setup():

    core.WINDOW_SIZE=[900, 600]
    core.fps = 60
    core.memory("etat", Etat.MENU)


def afficherMENU():
    pass


def afficherJEUX():
    pass


def afficherGAMEOVER():
    pass


def run():
    core.cleanScreen()


    if core.memory("etat") == Etat.MENU:
        afficherMENU()

    if core.memory("etat") == Etat.JEUX:
        afficherJEUX()

    if core.memory("etat") == Etat.GAMEOVER:
        afficherGAMEOVER()

core.main(setup,run)