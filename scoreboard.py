from turtle import Turtle
FONT_NAME = "Courier"  # Verdana
FONT_SIZE = 16
FONT_WEIGHT = "normal"
ALIGNMENT = "center"


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
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
