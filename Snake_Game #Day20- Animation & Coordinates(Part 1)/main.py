import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# to control display/frequency time for visibility


my_screen = Screen()
# creates an object from class Screen
my_screen.setup(width=600, height=600)
# display screen setup argument
my_screen.bgcolor("black")
# set screen background colour
my_screen.title("My snake Game")
# gives tittle to the screen
my_screen.tracer(0)
# turn off background animation display
my_screen.update()
# updates screen to display final results after backend animation

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.right, "Right")
my_screen.onkey(my_snake.left, "Left")

game_on = True

while game_on:
    my_screen.update()
    time.sleep(0.2)
    my_snake.move()

    # detect collision of snake with food

    if my_snake.snake_head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_score.increase_score()

    # detect collision with wall
    if my_snake.snake_head.xcor() > 280 or my_snake.snake_head.xcor() < -280 or my_snake.snake_head.ycor() > 280 or my_snake.snake_head.ycor() < -280:
        game_on = False
        my_score.game_over()

    # detect collision with the tail:
    for segment in my_snake.my_snake_segments[1:]:
        if my_snake.snake_head.distance(segment) < 10:
            game_on = False
            my_score.game_over()
    # if the head collides with any segment oin the tail:
    # trigger game_over

my_screen.exitonclick()
# to set screen to exist only on click
