# A = range(1, 10)
# print(* A)
# for x in A:
#     print(x)

# A = [(1,10), (2,20), (3,30)]
# print(len(A))
# for first, second in A:
#     print(first, second)

from turtle import *
t.shape('turtle')
t.color('blue', 'red')

# def one():
#     goto()
#     penup()
#     setpos(x, y + 30)
#     pendown()
#     setpos(x + 30, y + 60)
#     setpos(x + 30, y)
#     penup()
#     setpos(x + 30, y)
# one()
# fd = 10
n = 100
def ht():
    for z in range(n):
        dot()
        fd(30)
        rt(z)
ht()




t.done()
