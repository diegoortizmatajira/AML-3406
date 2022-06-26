from tkinter import *
from tkinter import ttk


def run():
    # declare the window
    window = Tk()
    # set window title
    window.title("Classroom Diagnostic Application - AML-3406")
    # set window width and height
    window.configure(width=800, height=600)
    # set window background color
    window.config
    frm = ttk.Frame(window, padding=10)
    frm.grid()
    ttk.Label(
        frm,
        text=
        "Welcome to the Classroom Diagnostic Application. It will allow you to measure the student's attentiveness"
    ).grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
    window.mainloop()
