import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

##1.先建立player > 進player函數
##2.建立car_manager函數


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ##每一次畫面更新就產出車輛,所以放下面
    car_manager.create_car()
    car_manager.moving()

    ###玩家跟車輛的距離小於20 就gameover
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        ###玩家到終點level up 車輛速度加快
        if player.final_line():
            player.go_to()
            scoreboard.increace_score()
            car_manager.level_up()

screen.exitonclick()
