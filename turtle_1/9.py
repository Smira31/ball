import math
import turtle as t

t.shape('turtle')
t.color('green', 'red')
t.speed(1)

loops = 0
n = 3
r = 15


def polygon(n, L):
    a = (n - 2) * 180  / n
    for i in range(n):
        t.left(180 - a)
        t.forward(L)
for loops in range(10):
    L = 2 * r * math.sin(math.pi / n)
    ang = ((n - 2) * 180/n) / 2
    t.left(ang)
    polygon(n, L)
    t.right(ang)
    t.penup()
    t.forward(15)
    t.pendown()
    r += 15
    n += 1
    loops += 1






t.done()
