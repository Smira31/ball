from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('600x300+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']


def paint(event):
    k = 0
    canv.delete(ALL)
    while color != 'red':
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(10, 70)
        color = choice(colors)
        canv.create_oval(x - r, y - r, x + r, y + r, fill=color)


canv.bind('<Button-1>', paint)
mainloop()

canv.bind('<Button-1>',paint)
root.mainloop()
