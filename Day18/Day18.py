# Day 18


from turtle import Turtle,Screen



jimmy=Turtle()
screen=Screen()
screen.colormode(255) # to access RGB color



# Drawing a square
def square():
    for i in range(4):
        jimmy.forward(100)
        jimmy.left(90)

square()


# Drawing a dashed line
for i in range(10):
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)
    jimmy.pendown()


# Drawing shapes using turtle
import random        
colors=["red","orange","blue","purple","green","black","cyan","brown"]
def draw_Shape(sides):
    for i in range(sides):
        angle=360/sides
        jimmy.forward(50)
        jimmy.left(angle)
        

for j in range(3,11):
    jimmy.color(random.choice(colors))
    draw_Shape(j)


# Generating random walk - method 1
import random
colors=["red","orange","blue","purple","green","black","cyan","brown"]
direction=["forward","backward","left","right"]
jimmy.shape(name="circle")
jimmy.pensize(20)


for i in range(100):
    choose_dirn=random.choice(direction)
    choose_color=random.choice(colors)
    jimmy.color(choose_color)
    if choose_dirn=="forward":
        jimmy.forward(50)
    elif choose_dirn=="backward":
        jimmy.backward(50)
    elif choose_dirn=="left":
        jimmy.left(90)
    elif choose_dirn=="right":
        jimmy.right(90)



# Method-2
import random
colors=["red","orange","blue","purple","green","black","cyan","brown"]
jimmy.pensize(20)
angle=[0,90,180,270]
for i in range(100):
    jimmy.color(random.choice(colors))
    jimmy.forward(50)
    jimmy.setheading(random.choice(angle))

# Method-3

import random
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

jimmy.pensize(20)   
angle=[0,90,180,270]
for i in range(200):
    jimmy.color(random_color())
    jimmy.forward(50)
    jimmy.setheading(random.choice(angle))
    


# Python tuples - data type which is immutable and ordered used to store heterogeneous data types in ()
a=(11,84,829,True,"Hello",98.1)
b=(1,2,3,4,5,6,7)
c=(1,) # single element tuple 


# Spirograph

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

def draw_spirograph(gap):
    for i in range(int(360/gap)):
        jimmy.speed("fastest")
        jimmy.color(random_color())
        jimmy.circle(100)
        current_heading=jimmy.heading()
        jimmy.setheading(current_heading+gap)
        

draw_spirograph(20)



screen.exitonclick()    


    

    

















