import turtle

def draw_light(start_pos=[0, 0], color="yellow", scale=1, seth=0):
    turtle.pencolor("#333333")
    turtle.pensize(2)

    turtle.fillcolor(color)


    turtle.penup()
    turtle.seth(seth)
    turtle.goto(start_pos[0], start_pos[1])
    turtle.pendown()

    turtle.begin_fill()

    turtle.circle(30/scale, 300)

    turtle.rt(48)
    turtle.fd(25/scale)
    turtle.lt(60)
    turtle.circle(30/scale, 40)
    turtle.goto(start_pos[0], start_pos[1])

    turtle.end_fill()
