# coding=utf-8

import turtle


def draw_bear(start_pos=[0, 0], scale=1):
    turtle.seth(0)
    turtle.pensize(3/scale)
    turtle.pencolor("black")

    # 棕色圈
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])
    turtle.pendown()

    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.circle(100/scale)
    turtle.end_fill()

    # 白色圈
    turtle.penup()

    turtle.goto(start_pos[0], start_pos[1] + 50/scale)

    turtle.pendown()

    turtle.fillcolor("white")

    turtle.begin_fill()
    turtle.pencolor("white")
    turtle.circle(30/scale)
    turtle.end_fill()

    turtle.pencolor("black")

    # 右眼
    turtle.penup()

    turtle.goto(start_pos[0], start_pos[1] + 50/scale + 30/scale)

    turtle.left(45)

    turtle.fd(35/scale)

    turtle.right(45)

    turtle.pendown()

    turtle.fillcolor("black")

    turtle.begin_fill()

    turtle.circle(10/scale)

    turtle.end_fill()

    # 左眼

    turtle.penup()

    turtle.goto(start_pos[0], start_pos[1] + 50/scale + 30/scale)

    turtle.lt(135)

    turtle.fd(35/scale)

    turtle.rt(135)

    turtle.pd()

    turtle.fillcolor("black")

    turtle.begin_fill()

    turtle.circle(10/scale)

    turtle.end_fill()

    # 鼻子,小圆

    turtle.penup()

    turtle.goto(start_pos[0], start_pos[1] + 50/scale + 30/scale)

    turtle.pd()

    turtle.fillcolor("black")

    turtle.begin_fill()

    turtle.circle(6/scale)

    turtle.end_fill()

    # 左斜

    turtle.goto(start_pos[0]-3/scale, start_pos[1] + 50/scale + 30/scale)

    turtle.seth(-135)

    turtle.pensize(5/scale)

    turtle.fd(12/scale)

    # 右斜

    turtle.penup()

    turtle.goto(start_pos[0] + 3/scale, start_pos[1] + 50/scale + 30/scale)

    turtle.pd()

    turtle.seth(-45)

    turtle.pensize(5/scale)

    turtle.fd(12/scale)


    # 右耳

    turtle.pensize(3/scale)

    turtle.penup()

    turtle.goto(start_pos[0], start_pos[1] + 100/scale)

    turtle.seth(30)

    turtle.fd(100/scale)

    turtle.pd()

    turtle.fillcolor("brown")

    turtle.begin_fill()

    turtle.circle(30/scale, 215)

    turtle.end_fill()

    # 左耳

    turtle.pu()

    turtle.goto(start_pos[0], start_pos[1] + 100/scale)

    turtle.seth(150)

    turtle.fd(100/scale)

    turtle.pd()

    turtle.fillcolor("brown")

    turtle.begin_fill()

    turtle.circle(-30/scale, 215)

    turtle.end_fill()