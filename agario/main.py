import core
from agario.map import Map

from agario.partie import Partie


def setup():
    print("Start_setup")
    core.WINDOW_SIZE= [1000,800]
    core.fps=80

    core.memory("partie",Partie())
    core.memory("partie").addPlayer()
    core.memory("partie").addBots()

    print("End_setup")



def run():
    print("Start_run")
    core.cleanScreen()
    core.memory("partie").show()

    print("End_run")

core.main(setup,run)

