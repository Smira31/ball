from turtle import *
from random import randrange as rnd
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'black', 'gray', 'lightgreen']

speed(5)
pu()
def krug(number_of):
    number = rnd(10 ,30)
    for i in  range(number):
        color(colors[rnd(len(colors))], colors[rnd(len(colors))])
        x = rnd(-200, 200)
        y = rnd(-200, 200)
        setpos(x, y)
        pd()
        begin_fill()
        circle(rnd(10, 100))
        end_fill()
        pu()

krug(rnd(10, 30))