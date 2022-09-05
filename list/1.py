from turtle import *
from random import randrange as rnd
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'black', 'gray', 'lightgreen']

speed(5)
pu()
def squar(number_of):
    for x in range(10):
        color(colors[rnd(len(colors))], colors[rnd(len(colors))])
        x = rnd(-200, 200)
        y = rnd(-200, 200)
        setpos(x, y)
        rt(rnd(10, 100))
        pd()
        begin_fill()
        for x in range(4):

            fd(number_of)
            left(90)
        end_fill()
        pu()

squar(rnd(10, 100))

done()