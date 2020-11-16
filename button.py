from graphics import Rectangle,Point,Text,color_rgb
class Button:
    def __init__(self,x,y,w,h,text,toggle,func):
        self.text = Text(Point(x,y), text)
        self.rect = Rectangle(Point(x,y), Point(x+w, y+h))
        self.toggle = toggle
        self.pressed = False
        self.func = func
        
    def press(self):
        if(self.toggle):
            self.pressed = not self.pressed
        self.func(self.pressed)

    def draw(self,win):
        if(self.pressed):
            self.rect.setFill(color_rgb(170,170,170))
        else:
            self.rect.setFill(color_rgb(100,100,100))