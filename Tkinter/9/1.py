from tkinter import *

root = Tk()
root.geometry('800x600')
fr = Frame(root)
bt_paint = Button(fr, width=8, text='paint')
bt_clear = Button(fr, width=8, text='clear')

bt_paint.pack(side='left', padx=2)
bt_clear.pack(side='left', padx=2)

fr.pack(pady=5)
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH, expand=1)

fr.pack(pady=5)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


def clear(event):
    canv.delete(ALL)


def paint(event):
    canv.create_rectangle(30, 50, 120, 80, fill='green')


bt_paint.bind('<Button-1>', paint)
bt_clear.bind('<Button-1>', clear)
mainloop()
