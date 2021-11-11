from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.update_score(self.score)


    def update_score(self,score):
        self.clear()
        self.goto(x=0, y=260)
        self.write(f"Score: {score} ", True, align=ALIGNMENT, font=FONT)



