from turtle import *

hideturtle()

r = 140
pensize(10)
color('blue', 'red')
penup()
begin_fill()
home()
forward(r)
left(90)
pendown()
circle(r)
end_fill()
penup()
left(90)
color('blue', 'yellow')
begin_fill()
pendown()
forward(2*r)
left(120)
forward(2*r)
left(120)
forward(2*r)
left(120)
end_fill()
done()