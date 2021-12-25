# coding=utf-8

import turtle

def draw_stake(start_pos=[0, 0],
               pensize=2,
               fillcolor="#996600"):
    turtle.pencolor("black")
    turtle.pensize(pensize)

    turtle.fillcolor(fillcolor)
    turtle.begin_fill()

    turtle.penup()
    turtle.seth(-90)
    turtle.goto(start_pos[0]-20, start_pos[1])
    turtle.pendown()

    turtle.forward(200)
    turtle.lt(90)
    turtle.forward(40)
    turtle.lt(90)
    turtle.forward(200)
    turtle.lt(90)
    turtle.forward(40)

    turtle.end_fill()