from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("beige")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("arial",20,"normal"))
        self.goto(-100,250)
        self.write("Player 1",align="center",font=("arial",20,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("arial",20,"normal"))
        self.goto(100,250)
        self.write("Player 2",align="center",font=("arial",20,"normal"))

    def winner(self):
        self.goto(0, 0)
        if self.l_score == 10:
            self.write("Player 1 Wins!", align="center", font=("arial", 30, "normal"))
        if self.r_score == 10:
            self.write("Player 2 Wins!", align="center", font=("arial", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()