from turtle import Turtle

class Stick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.shapesize(0.5, 6)
        self.penup()
        self.goto(x=0, y=-150)

    def right(self):
        self.forward(20)

    def left(self):
        self.backward(20)
    
    