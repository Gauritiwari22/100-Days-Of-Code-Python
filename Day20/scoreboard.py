from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day20/data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center",font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day20/data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.refresh()
