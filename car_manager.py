import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(0,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            x_cor = 300
            y_cor = random.randint(-250,250)
            new_car.goto(x_cor,y_cor)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

