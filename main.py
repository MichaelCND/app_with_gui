from tkinter import *

root = Tk()
root.title('Nya_bot')
root.wm_attributes('-alpha', 1)
root.geometry('400x300')
Canvas = Canvas(root, width=400, height=300)
Canvas.pack()

enter = Entry(root)
Canvas.create_window(72, 285, window= enter)


root.mainloop()
