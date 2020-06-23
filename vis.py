from config import *
from tkinter import *

w = Tk()
w.overrideredirect(True)
w.geometry("{0}x{1}+0+0".format(w.winfo_screenwidth(), w.winfo_screenheight()))
c = Canvas(w, width=10000, height=10000)
c.pack()


for i in range(SIZE + 1):
    c.create_line(450, 50 + i * 10, 450 + SIZE * 10, 50 + i * 10)
for i in range(SIZE + 1):
    c.create_line(450 + i * 10, 50, 450 + i * 10, 50 + SIZE * 10)
