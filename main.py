from tablero import Tablero
from button import Button
from graphics import GraphWin, color_rgb, Rectangle, Point, Text

tablero = Tablero(15, 8)


butStart = Button(5, 5, 100, 40, "Start/Stop", True)
butWalls = Button(110, 5, 100, 40, "Walls", True)
butRobot = Button(215, 5, 100, 40, "Roboto", True)
butClear = Button(320, 5, 100, 40, "Clear", False)


def func_start(pressed):
    if(pressed):
        print(":)")
    else:
        print(":(")


def func_walls(pressed):
    if(pressed):
        print(":)")
    else:
        print(":(")


def func_robot(pressed):
    if(pressed):
        print(":)")
    else:
        print(":(")


def func_clear(pressed):
    setText("Tablero limpiado!")

butStart.setFunc()
butWalls.set
butRobot.draw(win)
butClear.draw(win)

info = Rectangle(Point(425,5),Point(745,45))
infoText = Text(info.getCenter(),"")

def main():

    tablero = Tablero(15, 8)
    global win 
    win = GraphWin("Practica 1 - Robotito :)", tablero.cols *
                   tablero.cell_size, tablero.rows*tablero.cell_size + 50)
    win.setBackground(color_rgb(192, 192, 192))
    tablero.draw(win)
    butStart.draw(win)
    butWalls.draw(win)
    butRobot.draw(win)
    butClear.draw(win)

    while True:
        point = win.getMouse()
        xpos = point.getX()
        ypos = point.getY()
        if(ypos > 50):
            tablero.toggle(xpos, ypos-50, win)
        else:
            if(butStart.isInside(xpos, ypos)): butStart.press(win)
            elif(butWalls.isInside(xpos, ypos)): butWalls.press(win)
            elif(butRobot.isInside(xpos, ypos)): butRobot.press(win)
            elif(butClear.isInside(xpos, ypos)): butClear.press(win)



    #win = GraphWin("My Circle", width, height)
    #square = Rectangle(Point(cell_size,cell_size), Point(width-cell_size, height-cell_size))
    #square.setFill(color_rgb(230, 230, 230))
    # square.draw(win)

    # for i in range(1, columns-1):
    #    line = Line(Point(i*cell_size,cell_size),Point(i*cell_size,height-cell_size))
    #    line.draw(win)
    # for j in range(1, rows-1):
    #    line = Line(Point(cell_size,j*cell_size),Point(width-cell_size,j*cell_size))
    #    line.draw(win)
        # for i in range(1, columns-1):
        #    for j in range(1, rows-1):
        #        square = Square(i, j, cell_size)
        #        square.draw(win)

    # while True:
    #    point = win.getMouse()
    #    posx = point.getX()
    #    posy = point.getY()
    #    click_col = math.floor(posx/cell_size)
    #    click_row = math.floor(posy/cell_size)
    #    card = Rectangle(Point(click_col*cell_size,click_row*cell_size),Point(click_col*cell_size+cell_size,click_row*cell_size+cell_size))
    #    card.setFill(color_rgb(192,192,192))
    #    card.draw(win)

    # win.getMouse() # Pause to view result
    # win.close()    # Close window when done

def setText(texto):
    infoText.setText(texto)
    infoText.undraw()
    infoText.draw(win)



main()
