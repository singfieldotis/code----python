from random import choice
from turtle import Screen, Turtle, back, backward, forward

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# make different shapes
# angle is 360 / number of sides
# start with triangle
# give each shape a random color

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range(250):
    tim.color(choice(colors))
    tim.pensize(15)
    tim.speed("fastest")
    tim.forward(30)
    tim.setheading(choice(directions))


screen = Screen()
screen.bye()
