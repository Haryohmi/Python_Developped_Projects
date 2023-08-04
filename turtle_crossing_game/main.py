import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car = CarManager()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move_car()

    # detect player collision with car
    for car in car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False







    screen.listen()
    screen.onkey(fun=player.up, key="Up")





































