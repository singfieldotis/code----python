from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.speed("fasturn")


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
