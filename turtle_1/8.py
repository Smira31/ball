import turtle as t

t.shape('turtle')
t.color('green', 'red')
t.speed(10)
x = 10
for i in range(100):
    for g in range(2):
        t.fd(x)
        t.left(90)
    x += 5
