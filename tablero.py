import math
#import square.py
from graphics import *

cell_size = 100
width = 1400
height = 900

columns = int(width/cell_size)
rows = int(height/cell_size)

def main():
    win = GraphWin("My Circle", width, height)
    win.setBackground(color_rgb(192,192,192))
    square = Rectangle(Point(cell_size,cell_size), Point(width-cell_size, height-cell_size))
    square.setFill(color_rgb(230, 230, 230))
    square.draw(win)
    
    for i in range(1, columns-1):
        line = Line(Point(i*cell_size,cell_size),Point(i*cell_size,height-cell_size))
        line.draw(win)
    for j in range(1, rows-1):
        line = Line(Point(cell_size,j*cell_size),Point(width-cell_size,j*cell_size))
        line.draw(win)  
        #for i in range(1, columns-1):
        #    for j in range(1, rows-1):
        #        square = Square(i, j, cell_size)
        #        square.draw(win)
 
    
    while True:
        point = win.getMouse()
        posx = point.getX()
        posy = point.getY()
        click_col = math.floor(posx/cell_size)
        click_row = math.floor(posy/cell_size)
        card = Rectangle(Point(click_col*cell_size,click_row*cell_size),Point(click_col*cell_size+cell_size,click_row*cell_size+cell_size))
        card.setFill(color_rgb(192,192,192))
        card.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()