from turtle import *

hideturtle()
# speed(0)
def draw_sq(size = 2, fill = 'red'):
    pensize(5)
    fillcolor(fill)
    color('black', fill)
    begin_fill()
    penup()
    home()
    forward(size/2)
    right(90)
    forward(size/2)
    pendown()
    right(90)
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

draw_sq(200, 'red')
draw_sq(140, 'blue')
draw_sq(80, 'green')
done()
