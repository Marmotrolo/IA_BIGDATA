import numpy.random
jugadores="manuel","vicky","dan","gabriel","mario"


def gruposrol(jugadores,**kwargs):
    for rol, cuantos in kwargs.items():
        numpy.random.shuffle(jugadores)
        print(rol,":", jugadores[:cuantos])


gruposrol(jugadores, lider=1, explorador=2, guerrero=2)