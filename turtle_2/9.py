from turtle import *
color('green')
pendown()
for r in range(10):
    for i in range(10):
        pendown()
        fd(10)
        dot()


    rt(90)
    fd(10)
    rt(90)
    for a in range(10):
        pendown()
        fd(10)
        

    rt(-90)
    fd(10)
    rt(-90)


done()