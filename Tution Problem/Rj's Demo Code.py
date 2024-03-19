from turtle import *

def draw_plane(x=0, y=0, dir='up', pln_color='red', bg_color='cyan'):
    pensize(2)
    speed(0)

    hideturtle()
    penup()
    goto(x-40, y-40)
    setheading(0)
    pendown()
    fillcolor(bg_color)
    begin_fill()
    for i in range(4):
        forward(80)
        left(90)
    end_fill()
    penup()
    home()

    fillcolor(pln_color)

    if(dir == 'up'):
        goto(x-4, y-30)
    elif(dir == 'down'):
        goto(x+4, y+30)
        right(180)
    elif(dir=='right'):
        goto(x-30, y+4)
        right(90)

    begin_fill()
    pendown()
    left(100)
    forward(20)
    right(10)
    forward(35)
    circle(-6, 180)
    forward(35)
    right(10)
    forward(20)
    end_fill()
    begin_fill()
    circle(-2, 180)
    end_fill()
    begin_fill()
    # setheading(195)
    left(115) #radder
    forward(15)
    right(105)
    forward(5)
    right(50)
    forward(16)
    penup()
    # setheading(0)
    right(40)
    forward(8)
    pendown()
    right(40)
    forward(16)
    right(50)
    forward(5)
    right(105)
    forward(15)
    end_fill()

    penup()

    # home()
    if(dir=='up'):
        goto(x,y)
        setheading(0)
    elif(dir=='down'):
        goto(x,y)
        setheading(180)
    elif(dir=='right'):
        goto(x,y)
        setheading(-90)

    begin_fill()
    forward(6)
    right(90)
    forward(3)
    pendown()
    left(80)
    forward(22)
    left(100)
    forward(8)
    left(70)
    forward(23)
    left(20)
    penup()
    forward(13)
    pendown()
    left(20)
    forward(23)
    left(70)
    forward(8)
    left(100)
    forward(22)
    right(10)
    end_fill()

clearscreen()
draw_plane(0,0,'down', 'green', 'yellow')

x=[-80,80]
y=[-80,80]

arro = ['up', 'right', 'down']
clr = ['red', 'green', 'blue', 'cyan', 'black']

d = 0

for i in x:
    for j in y:
        for l in range(1,2):
            draw_plane(i*l,j*l, arro[d%3], clr[d%4],clr[(d%4+1)])
            d+=1

draw_plane(240,-240,'right')