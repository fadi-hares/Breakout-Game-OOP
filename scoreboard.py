from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.speed(0)
        self.color('green')
        self.penup()
        self.hideturtle()
        self.goto(x=-370, y=180)
        self.write(f'Score: {self.x}', align='center', font=('Arial', 10, 'normal'))

    def increas_score(self):
        self.clear()
        self.x += 1
        self.write(f'Score: {self.x}', align='center', font=('Arial', 10, 'normal'))

    def win(self):
        self.clear()
        self.goto(0,0)
        self.color('white')
        self.write(f'You Win With Score: {self.x}', align='center', font=('Arial', 30, 'normal'))

    def lose(self):
        self.clear()
        self.goto(0,0)
        self.color('white')
        self.write(f'You lost With Score: {self.x}', align='center', font=('Arial', 30, 'normal'))
    
    