from tkinter import *

root =Tk()
root.geometry('800x600')
fr = Frame(root)

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH, expand=1)

def clear(event):
    canv.delete(ALL)

def paint(event):
    canv.create_rectangle(30, 50, 120, 80, fill='green')
    canv.create_line(10, 300, 300, 300, fill='blue', width=3)
    canv.create_rectangle(200, 200, 500, 500)
    r = 50
    canv.create_oval(300-r, 200-r, 300+r, 200+r, fill='red', width=3)
    canv.create_text(350, 350, text='Hello!')


canv.bind('<Button-1>', paint)
canv.bind('<Button-3>', clear)
mainloop()

