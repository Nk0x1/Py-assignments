#to do list
import tkinter
from tkinter import *


def add_task():
    task = entry.get()
    if task:
        task_list.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        pass

def complete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.itemconfig(selected_task, {'bg': 'red'})
    except IndexError:
        pass

window = tkinter.Tk()
window.title("To-Do List")
l1=Label(text="THIS IS YOUR TO DO LIST,Enter task below").grid(row=0,column=0)

entry = tkinter.Entry(window, font=("Times", 12))
entry.grid(row=1, column=0)


add_button = tkinter.Button(window, text="Add Task", command=add_task)
add_button.grid(row=1, column=1)

remove_button = tkinter.Button(window, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=0)

complete_button = tkinter.Button(window, text="Complete Task", command=complete_task)
complete_button.grid(row=3, column=1)

task_list = tkinter.Listbox(window, selectmode=tkinter.SINGLE, font=("Times", 12))
task_list.grid(pady=10)

window.mainloop()
