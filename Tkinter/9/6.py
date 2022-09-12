from tkinter import *
root =Tk()
fr = Frame(root)
root.geometry('300x300')
bt_paint = Button(root,width=8,text='paint')
bt_paint.pack()
canv = Canvas(root,bg='white')
canv.pack()
def paint(event):
    r =10
    canv.create_oval(50 -r,50-r,50+r,50+r,fill='red')
    bt_paint.bind('<Button>',paint)


bt_paint.bind('<Button-1>',paint)


mainloop()
