from graphics import Circle,Point,color_rgb
class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)

    def move(self,x,y):
        self.x = x
        self.y = y
        self.circle.undraw()
        self.circle = Circle(Point(x*50 + 25, y*50 + 50 +25), 20)

    def draw(self, win):
        self.circle.setFill(color_rgb(0,0,0))
        self.circle.undraw()
        self.circle.draw(win)