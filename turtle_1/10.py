import turtle as t

t.shape('turtle')
t.color('green', 'red')
for i in range(3):
    t.begin_fill()
    t.circle(100)
    t.circle(-100)
    t.left(360 / 6)
    t.end_fill()


t.done()