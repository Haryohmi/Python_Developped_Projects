from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # placing food randomly one the screen, within the 600 by 600 wall
        self.goto(random_x, random_y)

        # self.refresh()
    #
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # placing food randomly one the screen, within the 600 by 600 wall
        self.goto(random_x, random_y)
