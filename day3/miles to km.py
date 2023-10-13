import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Convert")
window.minsize(400,200)
l1=Label(text="Enter the distance in miles: ")
l1.grid(column=2,padx=150)
t=tkinter.Entry()
t.grid(column=2)
def c():
    i=int (t.get())
    ans=i*1.609
    l2.config(text=ans)

b1 =tkinter.Button(text = "Distance in kilometers",command=c )
b1.grid(column=2)
l2=Label()
l2.grid(column=2)
window.mainloop()