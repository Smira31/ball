import turtle as t

t.shape('turtle')
t.color('green', 'red')

radius = 50
t.left(90)
for i in range(20):
    t.circle(radius)
    t.circle(-radius)
    radius += 10




t.done()