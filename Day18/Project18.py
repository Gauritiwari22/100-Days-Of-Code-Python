"Project 18"

import colorgram
rgb_colors=[]
colors=colorgram.extract("Day18\hirst_image.jpg",30)

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

color_list=[(242, 239, 234), (229, 157, 77), (116, 166, 199), (41, 109, 155), (154, 63, 89), (237, 219, 228), 
            (24, 135, 100), (209, 133, 161), (220, 86, 61), (224, 237, 230), (211, 225, 235), (240, 199, 82), (112, 186, 157), 
            (200, 82, 110), (170, 163, 41), (239, 158, 183), (53, 170, 132), (173, 73, 52), (34, 164, 191), (112, 114, 170),
              (6, 109, 88), (123, 38, 51), (247, 163, 147), (149, 214, 198),(44, 58, 101), (30, 58, 78), (146, 207, 228), (177, 182, 216), (67, 45, 54), (65, 46, 44)]



from turtle import Turtle,Screen
import random



tod=Turtle()
screen=Screen()
screen.colormode(255)

tod.hideturtle()
tod.penup()

width=screen.window_width()
height=screen.window_height()

start_x=-width/2+40
start_y=-height/2+40

tod.speed("fastest")
tod.goto(start_x,start_y)


def structure():
    for i in range(10):
        tod.dot(40,random.choice(color_list))
        tod.forward(60)

for i in range(15):
    structure()
    start_y+=60
    tod.goto(start_x, start_y)


screen.exitonclick()
