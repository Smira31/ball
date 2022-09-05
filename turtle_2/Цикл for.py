from turtle import *
from random import randrange as rnd
speed(10)
width(2)
pendown()
def fig(n):
    for r in range(n):
        for z in range(n):
            forward(10)
            dot()
        forward(-10*(r +1))
        right(90)
        fd(10)
        rt(-90)
        rt(10)
n = 6
for v in range(n):
    fd(200 / n)
    rt(360/ n)





done()