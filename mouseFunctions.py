import win32api, win32con
import time
import random

# Left click at x,y coordinates
def Lclick(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# Right click at x,y coordinates
def Rclick(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

# Smoothly moves the cursor to x,y and then left click
def leftClick(x, y):
    smoothMouseMove(x, y)
    time.sleep(random.uniform(0.03, 1.0))
    Lclick(x, y)

# Smoothly moves the cursor to x,y and then right click
def rightClick(x, y):
    smoothMouseMove(x, y)
    time.sleep(random.uniform(0.03, 1.0))
    Rclick(x, y)

# A smoothly mouse moving function
def smoothMouseMove(xFinal, yFinal):
    xBegin = win32api.GetCursorPos()[0]
    yBegin = win32api.GetCursorPos()[1]

    distanceX = xFinal - xBegin
    distanceY = yFinal - yBegin
    if distanceX < 0:
        distanceX *= -1
    if distanceY < 0:
        distanceY *= -1

    if distanceX > distanceY:
        if distanceY != 0:
           moveY = distanceX / distanceY
        count = 1
        while xBegin != xFinal:
            time.sleep(0.001)
            if (xFinal - xBegin) >= 0:
                xBegin += 1
            else:
                xBegin -= 1
            if moveY and count >= moveY:
                if (yFinal - yBegin) >= 0:
                    yBegin += 1
                else:
                    yBegin -= 1
                count = 1
            win32api.SetCursorPos((xBegin, yBegin))
            count += 1
    else:
        if distanceX != 0:
            moveX = distanceY / distanceX
        else:
            moveX = False
        count = 1
        while yBegin != yFinal:
            time.sleep(0.001)
            if (yFinal - yBegin) >= 0:
                yBegin += 1
            else:
                yBegin -= 1
            if count >= moveX or moveX != False:
                if (xFinal - xBegin) >= 0:
                    xBegin += 1
                else:
                    xBegin -= 1
                count = 1
            win32api.SetCursorPos((xBegin, yBegin))
            count += 1
