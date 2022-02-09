from turtle import Screen, Turtle
from random import choice

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# make different shapes
# angle is 360 / number of sides
# start with triangle
# give each shape a random color

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
