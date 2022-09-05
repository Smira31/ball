import turtle as t

t.shape('turtle')
t.color('green', 'red')

t.penup()
t.goto(200, 200)
t.left(360 - 124)
for i in range(11):
    t.pendown()
    t.forward(200)
    t.left(163.5)