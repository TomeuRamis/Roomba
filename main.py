##################################################
# Sistemas Inteligentes - Práctica 1             #
# Bartomeu Ramis Tarragó y David Cantero Tirado  #
##################################################

from tablero import Tablero
from button import Button
from graphics import GraphWin, color_rgb, Rectangle, Point, Text
from tkRepeatingTask import TkRepeatingTask, BackgroundTask
import threading
import time
import graphics

numFilas = 9
numColumnas = 15
tablero = Tablero(numColumnas, numFilas)
paused = True
walls = False
roombas = False
roboThread = None

butStart = Button(5, 5, 100, 40, "Start/Stop", True)
butWalls = Button(110, 5, 100, 40, "Walls", True)
butRobot = Button(215, 5, 100, 40, "Robot", True)
butClear = Button(320, 5, 100, 40, "Clear", False)


def func_start(pressed):
    global paused
    if(pressed):
        if (tablero.hasRobot()):
            if (butRobot.pressed): butRobot.press(win)
            if (butWalls.pressed): butWalls.press(win)
            butClear.lock(win)
            paused = False
            global roboThread
            roboThread = TkRepeatingTask(graphics.getRoot(), roboFunc, 250)
            roboThread.start()
            #roboThread = threading.Thread(target=roboFunc)
            #roboThread.start()
            setText("")
        else:
            butStart.press(win)
            setText("Falta poner un robot")
    else:
        paused = True
        if tablero.hasRobot(): tablero.detach()
        if not roboThread is None : roboThread.stop()
        setText("")
        butClear.unlock(win)


def func_walls(pressed):
    global walls
    if(pressed):
        if (butRobot.pressed): butRobot.press(win)
        if (butStart.pressed): butStart.press(win)
        walls = True
    else:
        walls = False
    setText("")


def func_robot(pressed):
    global roombas
    if(pressed):
        if (butWalls.pressed): butWalls.press(win)
        if (butStart.pressed): butStart.press(win)
        roombas = True
    else:
        roombas = False
    setText("")


def func_clear(pressed):
    if (butStart.pressed): butStart.press(win)
    setText("Tablero limpiado!")
    tablero.clear()
    tablero.draw(win)

butStart.setFunc(func_start)
butWalls.setFunc(func_walls)
butRobot.setFunc(func_robot)
butClear.setFunc(func_clear)

info = Rectangle(Point(425,5),Point(745,45))
infoText = Text(info.getCenter(),"")

def main():
    global win 
    win = GraphWin("Practica 1 - Robot", tablero.cols *
                   tablero.cell_size, tablero.rows*tablero.cell_size + 50)
    win.setBackground(color_rgb(192, 192, 192))
    tablero.draw(win)
    butStart.draw(win)
    butWalls.draw(win)
    butRobot.draw(win)
    butClear.draw(win)

    win.bind("<Button-1>",mousepressHandler)
    win.bind("<B1-Motion>",mousedragHandler)
    
    while True:
        try:
            _ = win.getKey()
        except:
            break
    

def roboFunc():
    tablero.roboStep()
    tablero.drawRobot(win)

def setText(texto):
    infoText.setText(texto)
    infoText.undraw()
    infoText.draw(win)

def mousepressHandler(event):
    #print("Click en x:" + str(event.x) + " y: " + str(event.y))
    xpos = event.x
    ypos = event.y
    if(ypos > 50):
        if(roombas): tablero.setRobot(xpos, ypos-50, win)
        elif(walls): 
            tablero.startStroke(xpos, ypos-50)
            tablero.updateStroke(xpos, ypos-50, win)
    else:
        if(butStart.isInside(xpos, ypos)): butStart.press(win)
        elif(butWalls.isInside(xpos, ypos)): butWalls.press(win)
        elif(butRobot.isInside(xpos, ypos)): butRobot.press(win)
        elif(butClear.isInside(xpos, ypos)): butClear.press(win)

def mousedragHandler(event):
    xpos = event.x
    ypos = event.y
    if(xpos <= win.getWidth() and ypos <= win.getHeight() and xpos > 0 and ypos > 0):
        if(ypos > 50 and walls):
            tablero.updateStroke(xpos, ypos-50, win)

main()
