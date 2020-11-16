from graphics import Rectangle,Point,color_rgb

class Square:

    def __init__(self, x, y, size):
        self.col = x        #Igual no hace falta
        self.row = y        #Igual no hace falta
        self.size = size    #Igual no hace falta

        self.wall = False
        self.square = Rectangle(Point(x*size,y*size+50), Point(x*size+size, y*size+size+50))

    def toggle(self):
        self.wall = not self.wall

    def draw(self, win):
        if(self.wall):
            self.square.setFill(color_rgb(55, 55, 55))
        else:
            self.square.setFill(color_rgb(230,230,230))
        self.square.undraw()
        self.square.draw(win)

    def pintar(self):
        print("x: " + str(self.col) + " y: "+ str(self.row))

    def isWall(self):
        return self.wall
