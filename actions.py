import mouseFunctions as mf
import time
import random

coordenadasComida = [0, 0]
coordenadasHotkey = [0, 0]
coordenadasNorte = [0, 0]
coordenadasSul = [0, 0]
coordenadasDepot = [575, 335]  # sul

def setCoordenadasComida(x, y):
    coordenadasComida[0] = x
    coordenadasComida[1] = y

def setCoordenadasHotkey(x, y):
    coordenadasHotkey[0] = x
    coordenadasHotkey[1] = y

def setCoordenadasNorte(x, y):
    coordenadasNorte[0] = x
    coordenadasNorte[1] = y

def setCoordenadasSul(x, y):
    coordenadasSul[0] = x
    coordenadasSul[1] = y


def venderYasir():
    time.sleep(3)
    i = 0

    print ("teste")
    while i< 50:
        mf.Lclick(coordenadasNorte[0], coordenadasNorte[1])
        mf.Lclick(coordenadasSul[0], coordenadasSul[1])
        i += 1

def beginRunes():

    tempoMana = 300 + random.randint(-10, 30)

    time.sleep(3)
    # while 1:
    # Andar e voltar pro Depot
    mf.leftClick(coordenadasNorte[0], coordenadasNorte[1])
    time.sleep(random.uniform(1.03, 2.0))
    mf.leftClick(coordenadasSul[0], coordenadasSul[1])

    # Fazer primeira runa
    mf.smoothMouseMove(coordenadasHotkey[0], coordenadasHotkey[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Lclick(coordenadasHotkey[0], coordenadasHotkey[1])

    # Esperar
    time.sleep(random.uniform(2.0, 3.0))

    # Fazer segunda runa
    mf.Lclick(coordenadasHotkey[0], coordenadasHotkey[1])

    # Esperar
    time.sleep(random.uniform(2.0, 3.0))

    # Fazer terceira runa
    mf.Lclick(coordenadasHotkey[0], coordenadasHotkey[1])

    # Esperar
    time.sleep(random.uniform(2.0, 3.0))

    # # Abrir depot
    # mf.smoothMouseMove(coordenadasDepot[0], coordenadasDepot[1])
    # time.sleep(random.uniform(0.03, 1.0))
    # mf.Rclick(coordenadasDepot[0], coordenadasDepot[1])

    # Abrir baus e comer
    mf.smoothMouseMove(coordenadasComida[0], coordenadasComida[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Rclick(coordenadasComida[0], coordenadasComida[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Rclick(coordenadasComida[0], coordenadasComida[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Rclick(coordenadasComida[0], coordenadasComida[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Rclick(coordenadasComida[0], coordenadasComida[1])
    time.sleep(random.uniform(0.03, 1.0))
    mf.Rclick(coordenadasComida[0], coordenadasComida[1])

    time.sleep(tempoMana)
