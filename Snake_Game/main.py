from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

in_on = True
while in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 檢查蛇頭與食物接觸到,食物會不會更新位置
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increace_score()
        snake.extend()

    # 檢查蛇頭有沒有跟牆面接觸到
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    ###檢查蛇頭有沒有跟任何一個部位發生碰撞
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
screen.exitonclick()
