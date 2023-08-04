import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def new_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            d_car = Turtle("square")
            d_car.penup()
            d_car.shape("square")
            d_car.shapesize(1, 2)
            d_car.color(random.choice(COLORS))
            d_car.goto(280, random.randint(-250, 250))
            self.all_cars.append(d_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
