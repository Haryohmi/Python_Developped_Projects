from turtle import Turtle

# to control display/frequency time for visibility


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.my_snake_segments = []
        self.create_snake()
        self.snake_head = self.my_snake_segments[0]
        self.move()

    def create_snake(self):
        # set coordinates for starting position
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        my_snake = Turtle()
        my_snake.penup()
        my_snake.shape("square")
        my_snake.color("white")
        my_snake.goto(position)
        self.my_snake_segments.append(my_snake)


    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.my_snake_segments[-1].position())
    def move(self):

        for snakes in range(len(self.my_snake_segments) - 1, 0, -1):
            # range(len(my_snake_segments)= no of snakes
            # -1 = starting position, 0 =  stop position, -1 =  steps
            new_x = self.my_snake_segments[snakes - 1].xcor()
            new_y = self.my_snake_segments[snakes - 1].ycor()
            self.my_snake_segments[snakes].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() == DOWN:
            return
        self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() == UP:
            return
        self.snake_head.setheading(DOWN)

    #
    def right(self):
        if self.snake_head.heading() == LEFT:
            return
        self.snake_head.setheading(RIGHT)

    #
    def left(self):
        if self.snake_head.heading() == RIGHT:
            return
        self.snake_head.setheading(LEFT)

        # my_screen = Screen()
        # my_screen.listen()
        # my_screen.onkey(fun=up,key="w")
        # my_screen.onkey(fun=down,key="z")
        # my_screen.onkey(fun=right,key="d")
        # my_screen.onkey(fun=left,key="a")
