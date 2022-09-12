from tkinter import *
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


canv.create_rectangle(30, 40, 120, 80, fill='green')
canv.create_line(10,100,150,10,fill='blue',width=5)
canv.create_rectangle(200,200,500,500)
canv.create_oval(200,200,500,500)
canv.create_text(350,350,text='Hello!')
mainloop()
