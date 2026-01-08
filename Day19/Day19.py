"Day 19"

from turtle import Turtle,Screen

jordan=Turtle()
screen=Screen()


def change():
    jordan.color("red")
    jordan.shape("turtle")
    jordan.penup()
    jordan.forward(10)

screen.listen()
screen.onkey(key="space", fun=change)

# Taking function as inputs
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculation(n1,n2,func):
    return func(n1,n2)

print(calculation(5,10,add)) # We take add function as the input without the parenthesis

# calculation() is a higher order function as it is using other functions to show output


# Making the Etch-A-Sketch App


def front():
    jordan.forward(10)
def back():
    jordan.backward(10)
def clockwise():
    jordan.right(5)
def anticlockwise():
    jordan.left(5)
def clear():
    jordan.reset()

jordan.shape("turtle")
jordan.pensize(10)
screen.listen()
screen.onkey(key="w", fun=front)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anticlockwise)
screen.onkey(key="c", fun=clear)

# Instance is an object created from a class 
# Object state are the values stored in the attributes of the object/instance



screen.exitonclick()
