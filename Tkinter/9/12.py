
from tkinter import *
from random import randrange as rnd

root = Tk()
root.geometry('600x600+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH ,expand=1)
x = 300
y = 300
r = 18
def krug():
    global x
    x += 3
    canv.delete('ball')
    canv.create_oval(x+r,y-r,x-r,y+r,fill='lightblue',width=3)
    if x < 550 :
        root.after(30, krug)



krug()

root.mainloop()