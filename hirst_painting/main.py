# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


from random import choice, randint
import turtle as turtle_module

tim = turtle_module.Turtle()
turtle_module.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# user color_list initially as it was a Damien Hirst color pallette but decided to make random_color() generator instead
# color_list = [(216, 149, 90), (53, 106, 136), (151, 85, 55), (123, 162, 187), (143, 67, 93), (217, 86, 61), (202, 131, 155), (166, 151, 46), (53, 122, 86), (44, 38, 30), (198, 86, 117),
#              (27, 47, 69), (120, 179, 153), (229, 201, 115), (74, 160, 121), (39, 56, 108), (49, 34, 45), (27, 47, 37), (239, 161, 184), (120, 35, 56), (103, 120, 168), (49, 158, 178), (245, 167, 155), (9, 101, 75), (113, 43, 33), (155, 212, 188)]


tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_of_dots = int(
    input("How many dots would you like? Please enter a factor of 10: "))

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(20, random_color())
    tim.pu()
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
