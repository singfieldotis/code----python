from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# make a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
