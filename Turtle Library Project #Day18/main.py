import random
import turtle
from turtle import Turtle, Screen

my_work = Turtle()
my_work.speed("fastest")

# for _ in range(4):
#     my_work.forward(100)
#     my_work.right(90)

# for _ in range(15):
#
#     my_work.forward(10)
#     my_work.penup()
#     my_work.forward(10)
#     my_work.pendown()


# is_on = True
# num_sides = 3
# while is_on:
#     for _ in range(num_sides):
#         angle = (360 / num_sides)
#         my_work.right(angle)
#         my_work.forward(100)
#     if num_sides > 10:
#             is_on = False
#     else:
#         num_sides += 1

# for _ in range(50):
#     my_work.pendown()
#     my_work.pencolor("red")
#     my_work.forward(10)
#     my_work.penup()
#     my_work.forward(10)


# colors = ["black", "dim gray", "dark cyan", "firebrick" ]
# def draw_angle(num_of_sizes):
#     for _ in range(num_of_sizes):
#         angle = 360/num_of_sizes
#         my_work.forward(100)
#         my_work.right(angle)
#
# for size in range(3,11):
#     draw_angle(size)
#     my_work.pencolor(random.choice(colors))


# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_color = (r, g, b)
#     return my_color

# directions = [0, 90, 180, 270]
# my_work.pensize(15)
# my_work.speed("fastest")
# for n in range(200):
#     my_work.pencolor(random_color())
#     my_work.forward(30)
#     my_work.setheading(random.choice(directions))


# def draw_spirograph(size_of_gap):
#     for angle in range(int(360/size_of_gap)):
#         my_work.color(random_color())
#         my_work.circle(100)
#         my_work.setheading(my_work.heading() + size_of_gap)
#
# draw_spirograph(5)


# my_work.circle(20)
# my_work.color("red")

turtle.colormode(255)

colour_list = [(234, 229, 232), (237, 34, 108), (221, 232, 237), (147, 26, 66)]

# 10 by 10 spots, 20 in sizes, 50 in spaces
# def horizontal_drawing():

is_on = True
count = 0
my_work.setheading(225)
my_work.hideturtle()
my_work.penup()
my_work.fd(300)
my_work.setheading(0)
while is_on:
    for n in range(10):
        my_work.dot(20, random.choice(colour_list))
        my_work.fd(50)
        my_work.dot(20)
    my_work.left(90)
    my_work.fd(50)
    my_work.left(90)
    my_work.fd(500)
    my_work.right(180)
    count += 1
    if count == 10:
        is_on = False




screen = Screen()
screen.exitonclick()
