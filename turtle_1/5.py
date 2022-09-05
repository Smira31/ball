import turtle as t

t.shape('turtle')
t.color('green', 'red')

dlina = 10
x = 0
y = 0

for i in range(10):
    dlina += 10
    x -= 10
    y -= 10
    for step in range(4):
        t.pendown()
        t.fd(dlina * 2)
        t.left(90)
        t.penup()
    t.goto(x, y)


t.done()
