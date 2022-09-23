from turtle import Turtle, Screen
import turtle as t
import random
import colorgram as cg


def get_colors():
    """Extracts colors from an image and returns a list with 30."""
    colors = cg.extract('spot.jpg',30)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_t = (r, g, b)
        color_list.append(color_t)
    return color_list


def draw_row():
    tim.pendown()
    for dot in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        if dot != 9:
            tim.forward(50)
    tim.left(90)
    tim.forward(40)
    tim.setx(-250)
    tim.right(90)


rgb_colors = get_colors()
t.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("NavyBlue")
tim.penup()
tim.goto(-250, -250)
tim.dot(20, random.choice(rgb_colors))
for row in range(10):
    draw_row()

screen = Screen()
screen.exitonclick()

