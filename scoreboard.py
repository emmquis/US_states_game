from turtle import Turtle
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

        self.guessed = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-260, y=260)
        self.write(arg=f"Guessed: {self.guessed} out of 50", align="center", font=FONT)

    def increase_guess(self):
        self.guessed += 1
        self.update_score()

    def repeat_guess(self):
        self.goto(x=0, y=260)
        self.write(arg="Already Guessed", align="center", font=FONT)

    def incorrect_guess(self):
        self.goto(x=0, y=260)
        self.write(arg="Not a state", align="center", font=FONT)