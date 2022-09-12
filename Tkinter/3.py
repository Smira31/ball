from tkinter import *
from random import randrange as rnd
root = Tk()
root.geometry('600x600')

canv = Canvas(bg='lightgreen')
canv.pack(fill=BOTH, expand=1)

for x in range(40,600,20):
    canv.create_line(x, 40, x, 580, fill='gray')
    canv.create_text(x, 20, text=x, font="arial 8")
for y in range(40,600,20):
    canv.create_line(40,y,580,y,fill='gray')
    canv.create_text(20,y,text=y,font = 'Arial 8')
canv.create_line(40, 40, 580, 40, width=2, arrow='last')
canv.create_line(40,40,40,580,width=2,arrow='last')

# x1 = 100
# y1 = 100
# x2 = 120
# y2 = 120
# canv.create_rectangle(x1,y1,x2,y2)

canv.create_line(300, 220, 300, 380, fill='red', width=2)
canv.create_line(220,300, 380, 300, fill='red', width=2)

x = 300
y = 300
r = 100
canv.create_oval(x-r, y-r, x+r,y+r, width=3)

canv.create_rectangle(80,80, 120,120,)
canv.create_text(100,100, text='123')





mainloop()