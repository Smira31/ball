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


canv.create_rectangle(200,200,400,400,width=3)
r =50
canv.create_oval(200-r,200-r,200+r,200+r,width=3)
canv.create_oval(400-r,400-r,400+r,400+r,width=3)
canv.create_oval(400-r,200-r,400+r,200+r,width=3)
canv.create_oval(200-r,400-r,200+r,400+r,width=3)



mainloop()