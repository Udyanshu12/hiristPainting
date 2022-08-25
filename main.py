import turtle as t
import random as r

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
              (0, 0, 0), (202, 164, 109), (150, 75, 49), (52, 93, 124), (172, 154, 40)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20, r.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
