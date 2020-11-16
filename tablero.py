import math
from square import Square
from robot import Robot


class Tablero:

    def __init__(self, ncols, nrows):
        self.cols = ncols
        self.rows = nrows
        self.cell_size = 50
        self.width = ncols * self.cell_size
        self.height = nrows * self.cell_size
        self.cells = [[Square(i, j, self.cell_size)
                       for i in range(ncols)] for j in range(nrows)]
        self.robot = None

    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(win)

    def toggle(self, xpos, ypos, win):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)
        self.cells[row][col].toggle()
        self.cells[row][col].draw(win)

    def clear(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].square.undraw()
        self.cells = [[Square(i, j, self.cell_size)
                       for i in range(self.cols)] for j in range(self.rows)]
        self.robot.circle.undraw()
        self.robot = None

    def setRobot(self, xpos, ypos, win):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)
        if(not self.cells[row][col].isWall()):
            if(self.robot is None):
                self.robot = Robot(col,row)
            else:
                self.robot.move(col,row)
            self.robot.draw(win)