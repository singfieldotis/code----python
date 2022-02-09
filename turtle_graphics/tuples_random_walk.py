from random import choice, randint
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(250):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))


screen = t.Screen()
screen.exitonclick()
