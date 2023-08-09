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
scoreboard = Scoreboard()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # detect player collision with car
    for new_car in car.all_cars:
        if new_car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()



    # detect a successful crossing; this happens when the player surpasses the height limit
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()






    screen.listen()
    screen.onkey(fun=player.up, key="Up")
screen.exitonclick()





































