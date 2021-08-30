import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [90, 180, 270, 360]    
# tim.pensize(10)
tim.speed('fastest')

def spirograph(circles_num):
    step = 360 / circles_num

    for i in range(circles_num):
        tim.color(random_color())
        # tim.forward(20)
        tim.setheading(i * step)
        tim.circle(50)

spirograph(30)
t.Screen()
t.exitonclick()