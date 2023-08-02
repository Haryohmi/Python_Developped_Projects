from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.setposition(position)

    def paddle_move_up(self):
        new_x = 0
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def paddle_move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
