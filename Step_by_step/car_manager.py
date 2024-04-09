from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = [] ###建立列表all_cars
        self.car_speed = STARTING_MOVE_DISTANCE ###車子的初始速度

    def create_car(self):
        random_num = random.randint(1, 6) ##這是要讓產出的數量降為1/6
        if random_num == 1:              ##如果random_num == 1才會生產車輛
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(310, random.randint(-300, 240))
            new_car.setheading(180)
            self.all_cars.append(new_car) ###將new_car輸入到all_cars裡

    def moving(self):
        for car in self.all_cars:   ##從列表讀出car,這樣才能所有車都前進
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

