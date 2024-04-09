from turtle import Turtle
FONT = ("Courier", 8, "normal")

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def state_map(self, state, x_pos, y_pos):
        self.goto(x=x_pos, y=y_pos)
        self.write(arg=f"{state}", font=FONT)
