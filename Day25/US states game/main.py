import turtle
import pandas as pd

screen=turtle.Screen()

screen.title("US States Game")
image="Day25/US states game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

user_answer=screen.textinput(title="Guess the state",prompt="Enter the state's name:")

def get_onmouseclick_cor(x,y):
    print(x,y)

turtle.onscreenclick(get_onmouseclick_cor)

data=pd.read_csv("50_states.csv")

if user_answer==data["state"]:
    turtle.goto
    turtle.write


screen.mainloop()