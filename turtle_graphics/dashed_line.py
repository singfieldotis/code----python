from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# draw a dashed line
for _ in range(15):
    tim.pendown()  # tim.pd() does the same thing
    tim.forward(10)
    tim.penup()  # tim.pu() does the same thing
    tim.forward(10)


screen = Screen()
screen.exitonclick()
