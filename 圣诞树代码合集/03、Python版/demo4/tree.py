import turtle

turtle.speed(0)

def draw_tree(start_pos=[0, 0], scale=1, fill=True):
    turtle.seth(-95)
    turtle.pensize(2)
    turtle.pencolor("#333333")

    turtle.fillcolor("#66CC99")


    # 左边
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])
    turtle.pendown()

    if fill:
        turtle.begin_fill()

    turtle.circle(-300 / scale, 65)
    turtle.seth(-25)
    turtle.circle(65 / scale, 45)

    turtle.seth(-100)
    turtle.circle(-20 / scale, 45)
    turtle.seth(0)
    turtle.circle(50 / scale, 45)

    for i in range(4):
        turtle.seth(-97+4*i)
        turtle.circle(-20 / scale, 60)
        turtle.seth(0)
        turtle.circle(50 / scale, 45)

    turtle.seth(-60)
    turtle.circle(50 / scale, 31)

    # 右边
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])
    turtle.pendown()

    turtle.seth(-85)
    turtle.circle(300 / scale, 65)
    turtle.seth(180+25)
    turtle.circle(-65 / scale, 45)

    turtle.seth(-80)
    turtle.circle(20 / scale, 45)
    turtle.seth(180)
    turtle.circle(-50 / scale, 45)

    for i in range(4):
        turtle.seth(-83-4*i)
        turtle.circle(20 / scale, 60)
        turtle.seth(180)
        turtle.circle(-50 / scale, 45)

    turtle.seth(-120)
    turtle.circle(-50 / scale, 31)


    if fill:
        turtle.end_fill()

    # 丝带
    turtle.pensize(1.5)
    turtle.pencolor("#333333")

    turtle.fillcolor("#FFEC8B")

    turtle.seth(-95)
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])

    # 下边
    turtle.seth(-95)
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])
    if fill:
        turtle.begin_fill()
    turtle.circle(-300 / scale, 47)
    turtle.rt(-120)
    turtle.pendown()

    turtle.circle(270 / scale, 48)


    # 上边

    turtle.seth(-95)
    turtle.penup()
    turtle.goto(start_pos[0], start_pos[1])
    turtle.circle(-300 / scale, 46)
    turtle.rt(-120)
    turtle.pendown()

    turtle.circle(270 / scale, 46)
    if fill:
        turtle.end_fill()

