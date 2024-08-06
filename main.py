import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

finish_line_y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.cars_move()
    for car in car_manager.all_cars:
        if player.distance(car) < 23:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= finish_line_y:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()








screen.exitonclick()
