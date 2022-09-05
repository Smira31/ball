from turtle import *
from random import randrange as rnd
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'black', 'gray', 'lightgreen']

speed(5)
pu()

def rect(number_of):
    dlina_1 = rnd(20, 100)
    dlina_2 = rnd(10, 50)
    for i in range(10):
        color(colors[rnd(len(colors))])
        x, y = rnd(-200, 300), rnd(-200, 300)
        setpos(x, y)
        pd()
        begin_fill()
        for x in range(2):
            fd(dlina_1)
            rt(90)
            fd(dlina_2)
            rt(90)
        pu()
        end_fill()


rect(10)