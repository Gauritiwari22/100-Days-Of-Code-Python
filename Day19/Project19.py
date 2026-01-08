from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

user_bet=screen.textinput("Welcome to the race!","Which color do you think will win?")
print(f"Your choice: {user_bet}")

y_position=[-150,-100,-50,0,50,100,150]
color=["red","yellow","orange","blue","pink","purple","green"]
turtles=[]



for i in range(7):
    new_turtle= Turtle() 
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color[i])
    new_turtle.goto(-200,y_position[i])
    turtles.append(new_turtle)

    

if user_bet:
    race_on=True

while race_on:
    for i in turtles:
        i.forward(random.randint(1,10))
        if i.xcor()>230:
            winner=i.pencolor()
            race_on=False
            

if winner==user_bet:
    print(f"{winner} won. Your turtle won the race.")
else:
    print(f"{winner} won. Your turtle lost the race.")
        
    

screen.exitonclick()