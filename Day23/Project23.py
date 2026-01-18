"Turtle Crossing Capstone Project"

import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard


screen=Screen()
screen.setup(600,600)
screen.tracer(0)

player=Player()
car_manager=Cars()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward,key="space")
game_on=True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()