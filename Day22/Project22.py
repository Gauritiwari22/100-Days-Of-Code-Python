from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()


screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.downward)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.downward)

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>300 or ball.ycor()<-300:
        ball.bounce()

    









screen.exitonclick()