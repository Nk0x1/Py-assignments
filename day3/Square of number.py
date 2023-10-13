import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Sqaure")
window.geometry("400x300")
l1=Label(text="Enter a number: ")
l1.grid(row=0,column=0)
t=tkinter.Entry()
t.grid(row=2,column=0)
def c():
    i=int (t.get())
    sq=i*i
    l2.config(text=sq)

b1 =tkinter.Button(text = "Get the square of this number",command=c )
b1.grid(row=3,column=0)
l2=Label()
l2.grid(row=5,column=0)
window.mainloop()