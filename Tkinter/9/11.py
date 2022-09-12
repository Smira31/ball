from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('600x600+100+100')

canv = Canvas( bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
x = 300
y = 300
r = 18

def update():
    global x
    x += 1
    x -= 1
    canv.delete('ball')
    canv.create_oval(x-r,y-r,x+r,y+r,fill='orange', tag = 'ball')

    if x < 550 and x >50:
        root.after(30, update)


update()
root.mainloop()
