import turtle as t

t.shape('turtle')
t.color('green', 'red')
t.speed(10)
x = 0.5
for i in range(100):
    for g in range(30):
        t.fd(x)
        t.left(6)
    x += 1
