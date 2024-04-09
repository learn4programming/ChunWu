from turtle import Turtle


class Interface(Turtle):

    def __init__(self):
        super().__init__()

    def center_line(self):
        line = Turtle()
        line.hideturtle()
        line.pencolor("white")
        line.width(5)
        line.penup()
        line.goto(0, 300)
        line.setheading(270)

        for _ in range(15):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

