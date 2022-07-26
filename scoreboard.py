from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=('Arial', 16, 'normal'))
