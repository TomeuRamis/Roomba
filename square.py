from graphics import *

class Square:

    def __init__(self, x, y, size):
        self.col = x
        self.row = y
        self.square = Rectangle(Point(x*size,y*size), Point(x*size+size, y*size+size))
        self.void = False

    def filled(self):
        self.void = True

    def draw(self, win):
        if(self.void):
            self.square.setFill(color_rgb(230, 230, 230))
        else:
            self.square.setFill(color_rgb(192,192,192))
        self.square.draw(win)

    def getVoid(self):
        return self.void
