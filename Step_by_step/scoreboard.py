from turtle import Turtle,Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.updated_scoreboard()

    ###建立分數更新的函數
    def updated_scoreboard(self):
        self.write(f"level: {self.level}", align='left', font=FONT)

    def increace_score(self):
        self.level += 1
        self.clear()
        self.updated_scoreboard()

    def game_over(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-80, 0)
        self.write("GAME OVER", align='left', font=FONT)
