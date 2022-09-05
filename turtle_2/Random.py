from turtle import  *
from random import randrange as rnd
shape('turtle')


def squar_1(size):
    rt(rnd(360))
    color('red', 'lightblue')
    begin_fill()
    pendown()
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    penup()
    end_fill()
    x = rnd(-200, 200)
    y = rnd(-200, 200)
    setpos(x, y)

def squar_2(size):
    rt(rnd(360))
    color('red', 'lightblue')
    begin_fill()
    pendown()
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    penup()
    end_fill()
    x = rnd(-200, 200)
    y = rnd(-200, 200)
    setpos(x, y)

def squar_3(size):
    rt(rnd(360))
    color('red', 'lightblue')
    begin_fill()
    pendown()
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    penup()
    end_fill()
    x = rnd(-200, 200)
    y = rnd(-200, 200)
    setpos(x, y)




squar_1(10)
squar_2(20)
squar_3(30)
done()

