from turtle import Screen
from ball import Ball
from blocks import Blocks
from stick import Stick
from scoreboard import Scoreboard


window = Screen()
window.bgcolor('black')
window.setup(800,400)
window.title('Breakout')
window.tracer(0)

#classes
ball = Ball()
blocks = Blocks()
stick = Stick()
scoreboard = Scoreboard()

#listner
window.listen()
window.onkeypress(stick.right, key='Right')
window.onkeypress(stick.left, key='Left')

game_on = True
while game_on:
    window.update()
    ball.move()
    if len(blocks.blocks) != 0:
        for block in blocks.blocks:
            if ball.distance(block) < 30 and ball.ycor() > 110:
                ball.bounce_y()
                blocks.remove_block(block)
                scoreboard.increas_score()
    else:
        window.clear()
        window.bgcolor('black')
        scoreboard.win()
        game_on = False

    #bounce with egdes
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #bounce with floor
    if ball.ycor() > 180:
        ball.bounce_y()

    if ball.ycor() < -200:
        game_on = False
        scoreboard.lose()

    #bounce with stick
    if ball.distance(stick) < 40 and ball.ycor() < -140:
        ball.bounce_y()

#mainLoop
window.exitonclick()