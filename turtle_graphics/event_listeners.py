from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
