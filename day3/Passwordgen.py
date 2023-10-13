#password Generation
import random
import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("PASSWORD GENERATOR")
window.minsize(400,200)
l1=Label(text="Let's generate a password")
l1.pack()
l2=Label(text="How many letters would you like in your password?")
l2.pack()
t1=tkinter.Entry()
t1.pack()
l3=Label(text="How many symbols would you like")
l3.pack()
t2=tkinter.Entry()
t2.pack()
l4=Label(text="How many numbers would you like?")
l4.pack()
t3=tkinter.Entry()
t3.pack()
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def c():
    password_list = []
    nr_letters=int(t1.get())
    nr_symbols=int(t2.get())
    nr_numbers=int(t3.get())
    for char in range(0, nr_letters ):
       password_list += random.choice(letters)
    
    for char in range(0, nr_symbols ):
       password_list += random.choice(symbols)

    for char in range(0, nr_numbers):
       password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = ""
    for char in password_list:
       password += char
    
    l5=Label(text=password)
    l5.pack()
b=tkinter.Button(text="Submit and Generate password",command=c)
b.pack()





window.mainloop()