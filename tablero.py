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
        self.stroke = [[False for i in range(ncols)] for j in range(nrows)]
        self.strokeMode = True # True = Poner pared, False = Borrar pared
        self.robot = None

    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(win)

    def drawRobot(self, win):
        self.robot.draw(win)

    def toggle(self, xpos, ypos, win):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)

        if(not (self.robot is None) and col == self.robot.getCol() and row == self.robot.getRow()): self.robot = None
        self.cells[row][col].toggle()
        self.cells[row][col].draw(win)

    def startStroke(self, xpos, ypos):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)
        self.strokeMode = not self.cells[row][col].isWall()
        self.stroke = [[False for i in range(self.cols)] for j in range(self.rows)]

    def updateStroke(self, xpos, ypos, win):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)

        if not self.stroke[row][col] :
            if(self.robot is None or not(self.robot.getCol() == col and self.robot.getRow() == row)):
                self.stroke[row][col] = True
                self.cells[row][col].setWall(self.strokeMode)
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

    def hasRobot(self):
        return not (self.robot is None)

    def roboStep(self):
        roboX = self.robot.getCol()
        roboY = self.robot.getRow()
        x = [False, False, False, False, False, False, False, False]

        x[0] = roboX == 0 or roboY == 0 or self.cells[roboY-1][roboX-1].isWall() 
        x[1] = roboY == 0 or self.cells[roboY-1][roboX].isWall() 
        x[2] = roboX == self.cols-1 or roboY == 0 or self.cells[roboY-1][roboX+1].isWall() 
        x[3] = roboX == self.cols-1 or self.cells[roboY][roboX+1].isWall() 
        x[4] = roboX == self.cols-1 or roboY == self.rows-1 or self.cells[roboY+1][roboX+1].isWall() 
        x[5] = roboY == self.rows-1 or self.cells[roboY+1][roboX].isWall() 
        x[6] = roboX == 0 or roboY == self.rows-1 or self.cells[roboY+1][roboX-1].isWall() 
        x[7] = roboX == 0 or self.cells[roboY][roboX-1].isWall()
        self.robot.actualizarPercepciones(x)
        self.robot.razona()