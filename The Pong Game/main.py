from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scorebooard

screen = Screen()
# set screen object
screen.setup(800, 600)
# setup screen size
screen.bgcolor("black")
# set screen background colour to black
screen.tracer(0)
# to turn off animation, - needs screen update to display

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# set each paddle to a different position(left and right)


ball = Ball()
scoreboard = Scorebooard()
speed = 0.1


screen.title("Mayowa Pong Game")
game_on = True

while game_on:
    screen.update()
    # to display updated screen after animation turned off
    time.sleep(speed)
    # to control the pace of object movement (it's speed)
    ball.ball_move()


    # to detect collision with the y_axis wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.ball_bounce_y()

    # to detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()
        speed *= 0.9

    # when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboaord()

        # game_on = False

    # when l_paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboaord()

    # initiating the screen to listen to object control
    screen.listen()
    screen.onkey(r_paddle.paddle_move_up, "Up")
    screen.onkey(r_paddle.paddle_move_down, "Down")
    screen.onkey(l_paddle.paddle_move_up, "w")
    screen.onkey(l_paddle.paddle_move_down, "s")
    # to set a key to a function to control object on the screen

screen.exitonclick()
# to keep screen display on, until screen is clicked
