import turtle
from turtle import *
import colorsys

speed(9999999999999999999999999)
bgcolor("Black")
h = 0

for i in range(12):  # Increased to create more petals
    setheading(i * 30)  # Adjusting angle for each petal
    for j in range(20):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)

done()
