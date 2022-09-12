from tkinter import *
root = Tk()
root.geometry('500x500')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

canv.create_line(250, 0, 250, 500, fill='red', width=3)
canv.create_line(0, 250, 500, 250, fill='blue', width=3)
canv.create_rectangle(200, 200 ,300, 300, fill='yellow', width=3)
canv.create_oval(10, 10, 60, 60)
mainloop()
