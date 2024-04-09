from turtle import Turtle, Screen
from screen import Interface
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
game_is_on = True
interface = Interface()
interface.center_line()
l_score = Score((-70, 210))
r_score = Score((70, 210))

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #檢查球碰到上下方會反彈
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #球碰到球拍會反彈
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
       l_score.increase_score()
       ball.serve()

       if l_score.score == 7:
           game_is_on = False
           l_score.game_over()

    elif ball.xcor() < -360:
         r_score.increase_score()
         ball.serve()

         if r_score.score == 7:
            game_is_on = False
            r_score.game_over()

screen.exitonclick()