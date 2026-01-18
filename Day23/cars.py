import random
from turtle import Turtle


colors=["red","yellow","green","blue","pink","purple"]
START_MOVE_DISTANCE=5
MOVE_INCREMENT=10


class Cars:

    def __init__(self):
        self.all_cars=[]
        self.cars_speed=START_MOVE_DISTANCE

    def create_cars(self):
        random_chance=random.randint(1,4)
        if random_chance==1:
            car=Turtle(shape="square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.cars_speed)
    
    def level_up(self):
        self.cars_speed+=MOVE_INCREMENT

    