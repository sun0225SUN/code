# coding=utf-8

import turtle

def draw_star(star_len=5,
              start_pos=[0, 0],
              pencolor="#FFFF99",
              seth=0,
              pensize=2,
              fill=True,
              fillcolor="#FFFF99"):
    turtle.pencolor(pencolor)
    turtle.pensize(pensize)

    if fill:
        turtle.fillcolor(fillcolor)
        turtle.begin_fill()

    turtle.penup()
    turtle.seth(seth)
    turtle.goto(start_pos[0], start_pos[1])
    turtle.pendown()

    for _ in range(5):
        turtle.forward(star_len)
        turtle.left(72)
        turtle.forward(star_len)
        turtle.right(180-36)



    if fill:
        turtle.end_fill()




