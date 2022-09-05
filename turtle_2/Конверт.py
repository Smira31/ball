import turtle
from turtle import *
turtle.speed(1)


def six():
    x,y = pos()
    penup()
    setpos(x + 30, y + 60)
    pd()
    setpos(x, y + 30)
    setpos(x , y)
    setpos(x + 30, y)
    setpos(x + 30, y + 30)
    setpos(x, y+30)
    penup()
    setpos(x + 30, y)
def zero():
    x, y = pos()
    penup()
    setpos(x, y +60)
    pendown()
    setpos(x , y )
    setpos(x +30, y )
    setpos(x+30, y + 60)
    setpos(x, y + 60)
    penup()
    setpos(x+30, y)

    setpos(x, y+ 60)

six()
forward(10)
zero()

done()
