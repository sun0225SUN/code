# coding=utf-8

import turtle
from star import draw_star
from bear import draw_bear
from tree import draw_tree
from stake import draw_stake
from light import draw_light

turtle.screensize(1200, 800, "#FFFFCC")

# 画笔颜色
turtle.pencolor("#cc0033")

# 抬起画笔
turtle.penup()
# 画笔颜色、尺寸
turtle.pencolor("#cc0033")
turtle.pensize(5)

# 放下画笔
turtle.pendown()

# draw_star(star_len=100, start_pos=[0, 0], pencolor="#333333", pensize=2, fill=True)
# draw_star(star_len=80, start_pos=[5, -2], pencolor="#333333", pensize=2, fill=True)
# draw_bear(start_pos=[-50, -100], scale=0.5)

# 树干
draw_stake(start_pos=[0, -150])

# 树
draw_tree(start_pos=[0, 50], scale=1)
draw_tree(start_pos=[0, 75], scale=1.3)
draw_tree(start_pos=[0, 95], scale=1.65)
draw_tree(start_pos=[0, 105], scale=2.4)
draw_tree(start_pos=[0, 130], scale=3.2)

# 星星
draw_star(star_len=23, start_pos=[-30, 130], pencolor="#333333", pensize=2, fill=True)
draw_star(star_len=15, start_pos=[-19.5, 126.5], pencolor="#333333", pensize=2, fill=True)

# 小熊
draw_bear(start_pos=[-20, 30], scale=10)
draw_bear(start_pos=[60, -30], scale=10)
draw_bear(start_pos=[0, -135], scale=10)

# 彩灯
draw_light(start_pos=[-100, -165], color="#FF00FF", scale=5, seth=180)
draw_light(start_pos=[-50, -175], color="#FFFF00", scale=5, seth=210)
draw_light(start_pos=[-10, -175], color="#EE6363", scale=5, seth=250)
draw_light(start_pos=[60, -175], color="#9370DB", scale=5, seth=250)

draw_light(start_pos=[-100, -100], color="#FFFF00", scale=5, seth=180)
draw_light(start_pos=[-50, -100], color="#EE6363", scale=5, seth=210)
draw_light(start_pos=[-10, -80], color="#FF00FF", scale=5, seth=250)
draw_light(start_pos=[60, -120], color="#FFFF00", scale=5, seth=250)

draw_light(start_pos=[30, 0], color="#9370DB", scale=5, seth=0)
draw_light(start_pos=[-10, -50], color="#FFFF00", scale=5, seth=210)
draw_light(start_pos=[-30, 15], color="#FFFF00", scale=5, seth=150)

draw_light(start_pos=[0, 60], color="#EE6363", scale=5, seth=300)

turtle.done()