from turtle import Turtle

##導入Turtle模組


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    ###2.玩家角色設定
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    ###建立按鍵移動Up
    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_to(self):
        self.goto(STARTING_POSITION)

    def final_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False