import math
from square import Square

class Tablero:

    def __init__(self,ncols,nrows):
        self.cols = ncols
        self.rows = nrows
        self.cell_size = 50
        self.width = ncols * self.cell_size
        self.height = nrows * self.cell_size
        self.cells = [[Square(i,j,self.cell_size) for i in range(ncols)] for j in range(nrows)]

    def draw(self,win):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(win)
    
    def toggle(self,xpos,ypos,win):
        col = int(xpos / self.cell_size)
        row = int(ypos / self.cell_size)
        self.cells[row][col].toggle()
        self.cells[row][col].draw(win)