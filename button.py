from graphics import Rectangle,Point,Text,color_rgb

class Button:

    def __init__(self,x,y,w,h,text,toggle):       
        self.rect = Rectangle(Point(x,y), Point(x+w, y+h))
        self.text = Text(self.rect.getCenter(), text)
        self.toggle = toggle
        self.pressed = False
        self.func = None
        self.locked = False
        
    def press(self,win):
        if not self.locked:
            if(self.toggle):
                self.pressed = not self.pressed
            self.func(self.pressed)
            self.draw(win)

    def draw(self,win):
        if(self.pressed or self.locked):
            self.rect.setFill(color_rgb(100,100,100))
        else:
            self.rect.setFill(color_rgb(170,170,170))
        self.rect.undraw()
        self.rect.draw(win)
        self.text.undraw()
        self.text.draw(win)

    def isInside(self,x,y):
        xmin = self.rect.getP1().getX()
        ymin = self.rect.getP1().getY()
        xmax = self.rect.getP2().getX()
        ymax = self.rect.getP2().getY()
        return (xmin <= x <= xmax)and(ymin <= y <= ymax)

    def setFunc(self, func):
        self.func = func

    def lock(self, win):
        self.locked = True
        self.draw(win)

    def unlock(self, win):
        self.locked = False
        self.draw(win)
            