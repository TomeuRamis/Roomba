from graphics import Circle,Point,color_rgb
class Robot:

    def __init__(self, x, y):
        self.col = x
        self.row = y
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)
        self.s = [False, False, False, False, False, False, False, False]
        self.x = [False, False, False, False]

    def move(self,x,y):
        self.col = x
        self.row = y
        #self.circle.undraw()
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)

    def draw(self, win):
        self.circle.setFill(color_rgb(0,0,0))
        self.circle.undraw()
        self.circle.draw(win)

    def getCol(self):
        return self.col
    
    def getRow(self):
        return self.row

    def actualizarPercepciones(self, perc):
        self.s = perc
        self.x[0] = perc[1] or perc[2]
        self.x[1] = perc[3] or perc[4]
        self.x[2] = perc[5] or perc[6]
        self.x[3] = perc[7] or perc[0]
        
    def desplaza(self, dir):
        # 0 - norte
        # 1 - este
        # 2 - sur
        # 3 - oeste
        x = self.col
        y = self.row
        if (dir == 0):   self.move(x    , y - 1)
        elif (dir == 1): self.move(x + 1, y)
        elif (dir == 2): self.move(x    , y + 1)
        elif (dir == 3): self.move(x - 1, y)

    def razona(self):
        x = self.x
        if(not (x[0] or x[1] or x[2] or x[3])): self.desplaza(0) #Norte
        elif(x[0] and (not x[1])): self.desplaza(1) #Este
        elif(x[1] and (not x[2])): self.desplaza(2) #Sur
        elif(x[2] and (not x[3])): self.desplaza(3) #Oeste
        elif(x[3] and (not x[0])): self.desplaza(0) #Norte