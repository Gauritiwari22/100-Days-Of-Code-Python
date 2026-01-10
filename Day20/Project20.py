"Snake Game Project"

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Welcome to the SnakeGame!")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while_on=True
while while_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 23:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        while_on=False
        scoreboard.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            while_on=False
            scoreboard.game_over()

        




        
screen.exitonclick()