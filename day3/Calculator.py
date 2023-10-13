#Calculator
import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Calculator")
window.minsize(400,200)
font=("Young Sherif",18)
l1=Label(text="MY CALCULATOR - ",font=font)
l1.grid(row=1,column=1,padx=10)
exp=""
result=tkinter.StringVar()
expfield = Entry(window, textvariable=result)
expfield.grid(row=1,column=2)
def click(i):
    global exp
    exp=exp+str(i)
    result.set(exp)

def c():
    try:
        global exp
        ans = str(eval(exp))
        result.set(ans)
        exp = ""
    except:
        result.set("error")
        exp = ""
    
   
def clear():
    global exp
    exp=""
    result.set("")
    
       
b1=tkinter.Button(text="1",command=lambda:click(1))
b2=tkinter.Button(text="2",command=lambda:click(2))
b3=tkinter.Button(text="3",command=lambda:click(3))
b4=tkinter.Button(text="4",command=lambda:click(4))
b5=tkinter.Button(text="5",command=lambda:click(5))
b6=tkinter.Button(text="6",command=lambda:click(6))
b7=tkinter.Button(text="7",command=lambda:click(7))
b8=tkinter.Button(text="8",command=lambda:click(8))
b9=tkinter.Button(text="9",command=lambda:click(9))
b0=tkinter.Button(text="0",command=lambda:click(0))

b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=2,column=4)
b5.grid(row=3,column=4)
b6.grid(row=4,column=4)
b7.grid(row=2,column=5)
b8.grid(row=3,column=5)
b9.grid(row=4,column=5)
b0.grid(row=2,column=6)

ba=tkinter.Button(text="+",command=lambda:click('+'))
bs=tkinter.Button(text="-",command=lambda:click('-'))
bm=tkinter.Button(text="*",command=lambda:click('*'))
bd=tkinter.Button(text="/",command=lambda:click('/'))
be=tkinter.Button(text="=",command=c)
bclr=tkinter.Button(text="clr",command=clear)

ba.grid(row=3,column=6)
bs.grid(row=4,column=6)
bm.grid(row=2,column=7)
bd.grid(row=3,column=7)
be.grid(row=4,column=7)
bclr.grid(row=5,column=3)

window.mainloop()
