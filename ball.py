from turtle import Turtle, Screen
import random

SERVE = [1, -1]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.serve()
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """球碰到兩端y軸時,將y_move乘上-1,讓它往反方向移動"""
        self.y_move *= -1

    def bounce_x(self):
        """球碰到球拍時,將x_move乘上-1,讓它往反方向移動"""
        self.x_move *= -1.08


    def serve(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.x_move *= (random.choice(SERVE))
        self.y_move *= (random.choice(SERVE))


