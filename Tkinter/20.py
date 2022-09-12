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

w = 20
canv.create_oval(100-w,100-w,100+w,100+w,fill='yellow')
canv.create_line(240,240,115,110,fill='orange',width=5)
canv.create_oval(500-w,100-w,500+w,100+w,fill='yellow')
canv.create_line(370,230,485,110,fill='orange',width=5)
canv.create_oval(100-w,500-w,100+w,500+w,fill='yellow')
canv.create_line(240,360,115,490,fill='orange',width=5)
canv.create_oval(500-w,500-w,500+w,500+w,fill='yellow')
canv.create_line(370,360,490,490,fill='orange',width=5)



r = 100
canv.create_oval(300-r,300-r,300+r,300+r,fill='red',width=3)
canv.create_line(300,200,300,120,fill='red',width=5)
canv.create_line(300,400,300,470,fill='red',width=5)
canv.create_line(130,300,200,300,fill='red',width=5)
canv.create_line(400,300,470,300,fill='red',width=5)
s =30
canv.create_oval(300-s,100-s,300+s,100+s, fill='red',width=3)
canv.create_line(300,200,300,120,fill='red',width=5)
canv.create_oval(300-s,500-s,300+s,500+s, fill='red',width=3)
canv.create_oval(100-s,300-s,100+s,300+s, fill='red',width=3)
canv.create_oval(500-s,300-s,500+s,300+s, fill='red',width=3)
mainloop()