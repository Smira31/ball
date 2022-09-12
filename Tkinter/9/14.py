from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('600x300+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)


def click(event):
    k = 0
    canv.delete(ALL)
    colors = ['red', 'blue', 'yellow', 'green']
    color = ''

    while k < 2:
        color = choice(colors)
        x = 50
        y = 150
        d = 25
        if color == 'red':
            k += 10
        canv.create_oval(x, y, x + d, y + d, fill=color)


canv.bind('<1>', click)
root.mainloop()
