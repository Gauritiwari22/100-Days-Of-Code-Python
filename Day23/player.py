from turtle import Turtle


STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINAL_Y=290

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(STARTING_POSITION)
        

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor()>=FINAL_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
        
    



