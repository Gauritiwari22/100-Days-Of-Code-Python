from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.final_score()


    def final_score(self):
        self.write(f"Score={self.score}", align="center", font=("arial",20,"normal"))

    def update_score(self):
        self.score+=1
        self.clear()
        self.final_score()

    def game_over(self):
        self.goto(0,0)
        self.color("beige")
        self.write("GAME OVER!", align="center",font=("arial",30,"normal"))

        
