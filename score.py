from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()

    def game_over(self):
        if self.score == 7:
           self.goto(0,0)
           self.write("GAME OVER", align=ALIGNMENT, font=FONT)
