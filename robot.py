from graphics import Rectangle,Circle,Point,color_rgb
class Robot:
    NORTE = 0
    ESTE = 1
    SUR = 2
    OESTE = 3

    def __init__(self, x, y):
        self.col = x
        self.row = y
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)
        self.facing = self.NORTE
        self.face = self._getFace()
        self.attached = False
        self.s = [False, False, False, False, False, False, False, False]
        self.x = [False, False, False, False]

    def move(self,x,y):
        self.col = x
        self.row = y
        self.circle.undraw()
        self.face.undraw()
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)
        self.face = self._getFace()

    def draw(self, win):
        self.circle.setFill(color_rgb(0,0,0))
        self.face.setFill(color_rgb(0,0,0))
        self.circle.undraw()
        self.face.undraw()
        self.circle.draw(win)
        self.face.draw(win)

    def undraw(self):
        self.circle.undraw()
        self.face.undraw()

    def getCol(self):
        return self.col
    
    def getRow(self):
        return self.row

    def detach(self):
        self.attached = False

    def actualizarPercepciones(self, perc):
        self.s = perc
        self.x[0] = perc[1] or perc[2]
        self.x[1] = perc[3] or perc[4]
        self.x[2] = perc[5] or perc[6]
        self.x[3] = perc[7] or perc[0]
        
    def desplaza(self, dir):
        x = self.col
        y = self.row
        self.facing = dir
        if (dir == self.NORTE):   self.move(x    , y - 1)
        elif (dir == self.ESTE): self.move(x + 1, y)
        elif (dir == self.SUR): self.move(x    , y + 1)
        elif (dir == self.OESTE): self.move(x - 1, y)

    def razona(self):
        x = self.x
        s = self.s
        if(not (x[0] or x[1] or x[2] or x[3])): self.desplaza(self.NORTE)
        elif not self.attached:
            if x[0] and not s[3]: self.desplaza(self.ESTE)
            elif x[1] and not s[5]: self.desplaza(self.SUR)
            elif x[2] and not s[7]: self.desplaza(self.OESTE)
            elif x[3] and not s[1]: self.desplaza(self.NORTE)
            self.attached = True
        elif self.facing == self.SUR:
            if not s[3]: self.desplaza(self.ESTE)
            elif not s[5]: self.desplaza(self.SUR)
            elif not s[7]: self.desplaza(self.OESTE)
            elif not s[1]: self.desplaza(self.NORTE) 
        elif self.facing == self.NORTE:
            if not s[7]: self.desplaza(self.OESTE)
            elif not s[1]: self.desplaza(self.NORTE) 
            elif not s[3]: self.desplaza(self.ESTE)
            elif not s[5]: self.desplaza(self.SUR)
        elif self.facing == self.ESTE:
            if not s[1]: self.desplaza(self.NORTE) 
            elif not s[3]: self.desplaza(self.ESTE)
            elif not s[5]: self.desplaza(self.SUR)
            elif not s[7]: self.desplaza(self.OESTE)
        elif self.facing == self.OESTE:
            if not s[5]: self.desplaza(self.SUR)
            elif not s[7]: self.desplaza(self.OESTE)
            elif not s[1]: self.desplaza(self.NORTE) 
            elif not s[3]: self.desplaza(self.ESTE)

    def _getFace(self):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        if (self.facing == self.NORTE):
            x1 = self.col * 50 + 20
            y1 = self.row * 50 + 50
            x2 = x1 + 10
            y2 = y1 + 10
        elif (self.facing == self.ESTE):
            x1 = self.col * 50 + 40
            y1 = self.row * 50 + 20 + 50
            x2 = x1 + 10
            y2 = y1 + 10
        elif (self.facing == self.SUR):
            x1 = self.col * 50 + 20
            y1 = self.row * 50 + 40 + 50
            x2 = x1 + 10
            y2 = y1 + 10
        elif (self.facing == self.OESTE):
            x1 = self.col * 50
            y1 = self.row * 50 + 20 + 50
            x2 = x1 + 10
            y2 = y1 + 10
        return Rectangle(Point(x1,y1),Point(x2,y2))
