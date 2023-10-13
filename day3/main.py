import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Hello,World!")

window.minsize(400,200) 
t=tkinter.Label(window,text="Hello world")
t.pack()
window.mainloop()