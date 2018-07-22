import win32api, win32con
import time
import random

def Lclick(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def Rclick(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

def moverMouse(xFinal, yFinal):
    xInicial = win32api.GetCursorPos()[0]
    yInicial = win32api.GetCursorPos()[1]

    distanciaX = xFinal - xInicial
    distanciaY = yFinal - yInicial
    if distanciaX < 0:
        distanciaX *= -1
    if distanciaY < 0:
        distanciaY *= -1

    if distanciaX > distanciaY:
        if distanciaY != 0:
            andarY = distanciaX / distanciaY
        cont = 1
        while xInicial != xFinal:
            time.sleep(0.001)
            if (xFinal - xInicial) >= 0:
                xInicial += 1
            else:
                xInicial -= 1
            if andarY and cont >= andarY:
                if (yFinal - yInicial) >= 0:
                    yInicial += 1
                else:
                    yInicial -= 1
                cont = 1
            win32api.SetCursorPos((xInicial, yInicial))
            cont += 1
    else:
        if distanciaX != 0:
            andarX = distanciaY / distanciaX
        else:
            andarX = False
        cont = 1
        while yInicial != yFinal:
            time.sleep(0.001)
            if (yFinal - yInicial) >= 0:
                yInicial += 1
            else:
                yInicial -= 1
            if cont >= andarX or andarX != False:
                if (xFinal - xInicial) >= 0:
                    xInicial += 1
                else:
                    xInicial -= 1
                cont = 1
            win32api.SetCursorPos((xInicial, yInicial))
            cont += 1

# norteCoord = [575, 260]
# sulCoord = [575, 335]
# lesteCoord = [625, 300]
# oesteCoord = [545, 300]

def leftClick(x, y):
    moverMouse(x, y)
    time.sleep(random.uniform(0.03, 1.0))
    Lclick(x, y)

def rightClick(x, y):
    moverMouse(x, y)
    time.sleep(random.uniform(0.03, 1.0))
    Rclick(x, y)

def rightClickNorte():
    moverMouse(norteCoord[0], norteCoord[1])
    time.sleep(random.uniform(0.03, 1.0))
    Rclick(norteCoord[0], norteCoord[1])

def leftClickSul():
    moverMouse(sulCoord[0], sulCoord[1])
    time.sleep(random.uniform(0.03, 1.0))
    Lclick(sulCoord[0], sulCoord[1])

def rightClickSul():
    moverMouse(sulCoord[0], sulCoord[1])
    time.sleep(random.uniform(0.03, 1.0))
    Rclick(sulCoord[0], sulCoord[1])