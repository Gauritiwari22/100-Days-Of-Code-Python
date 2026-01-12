from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.downward)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.downward)

game_on=True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_in_y()
        
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_in_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()
        if scoreboard.l_score == 10:
            scoreboard.winner()
            game_on = False

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()
        if scoreboard.r_score == 10:
            scoreboard.winner()
            game_on = False

    
screen.exitonclick()