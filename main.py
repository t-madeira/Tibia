import actions

from pynput.mouse import Listener

coordenadas = [0, 0]
def on_click(x, y, button, pressed):
    coordenadas[0]=x
    coordenadas[1]=y
    return False

from appJar import gui

def makeRunes():
    actions.beginRunes()

def vender():
    actions.venderYasir()

# handle button events
def comecarRunar(button):
    if button == "Start":
        x = 300
        app.setPollTime(x)
        app.registerEvent(actions.beginRunes())

def venderYasir(button):
    if button == "Start":
       app.registerEvent(vender)

def pegarCoordenadasDoClick(button):
    with Listener(on_click=on_click) as listener:
        listener.join()
    print(coordenadas)
    if button == "Definir coordenadas hotkey":
        app.setLabel("coordenadasHotkey2", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
        actions.setCoordenadasHotkey(coordenadas[0], coordenadas[1])
    elif button == "Definir coordenadas comida":
        app.setLabel("coordenadasComida2", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
        actions.setCoordenadasComida(coordenadas[0], coordenadas[1])
    elif button == "Definir coordenadas norte":
        app.setLabel("coordenadasNorte2", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
        actions.setCoordenadasNorte(coordenadas[0], coordenadas[1])
    elif button == "Definir coordenadas sul":
        app.setLabel("coordenadasSul2", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
        actions.setCoordenadasSul(coordenadas[0], coordenadas[1])
    return

# create a GUI variable called app
app = gui("Runador")
app.setFont(10)

app.addLabel("coordenadasHotkey", "Coordenadas da Hotkey: ", 0, 0)
app.addLabel("coordenadasHotkey2", "[0, 0]", 0, 1)
app.addButton("Definir coordenadas hotkey", pegarCoordenadasDoClick, 0, 2)

app.addLabel("coordenadasComida", "Coordenadas da Comida: ", 1, 0)
app.addLabel("coordenadasComida2", "[0, 0]", 1, 1)
app.addButton("Definir coordenadas comida", pegarCoordenadasDoClick, 1, 2)

app.addLabel("coordenadasNorte", "Coordenadas do Norte: ", 2, 0)
app.addLabel("coordenadasNorte2", "[0, 0]", 2, 1)
app.addButton("Definir coordenadas norte", pegarCoordenadasDoClick, 2, 2)

app.addLabel("coordenadasSul", "Coordenadas do Sul: ", 3, 0)
app.addLabel("coordenadasSul2", "[0, 0]", 3, 1)
app.addButton("Definir coordenadas sul", pegarCoordenadasDoClick, 3, 2)

app.addButton("Start", comecarRunar, 4, 2)

# start the GUI
app.go()

