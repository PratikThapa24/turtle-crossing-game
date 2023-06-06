import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(fun=player.moveup, key="Up")
screen.onkeypress(fun=player.movedown, key = "Down")

cars = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    #Detect Collision between car and collision
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()
    #Detect when turtle reaches the end
        if player.ycor() == 280:
            scoreboard.update_scoreboard()
            player.initial_position()
            cars.increase_speed()

screen.exitonclick()

