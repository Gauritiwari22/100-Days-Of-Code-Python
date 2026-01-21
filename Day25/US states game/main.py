import turtle
import pandas as pd

screen=turtle.Screen()

screen.title("US States Game")
image="Day25/US states game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


data=pd.read_csv("Day25/US states game/50_states.csv")
all_states=data.state.to_list()

guessed_states=[]

while len(guessed_states)<50:

    user_answer=screen.textinput(title="Guess the state",prompt="Enter the state's name:").title()
    state_cor=data[data.state==user_answer]

    if user_answer=="Exit":
        
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        learnings=pd.DataFrame(missing_states)        
        learnings.to_csv("Day25/US states game/States_to_learn.csv")
        
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        jim=turtle.Turtle()
        jim.hideturtle()
        jim.penup()
        jim.goto(state_cor.x.item(),state_cor.y.item())
        jim.write(state_cor.state.item())


screen.mainloop()