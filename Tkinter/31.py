from tkinter import *

root = Tk()
root.geometry('600x600+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)

x = 300
y = 300
r = 18

vx = 2

def update():
    global x
    x += vx
    canv.delete('ball')
    canv.create_oval(x - r, y - r, x + r, y + r, fill='orange', tag='ball')
    if x > 550:
        vx *= -1
        x = 550
    if x < 50:
        vx *= -1
        x = 50
    canv.delete('ball')
    canv.create_oval(x - r, y - r, x + r, y + r, fill='orange', tag='ball')

    root.after(30, update)



canv.bind('<1>', click)
update()
root.mainloop()
