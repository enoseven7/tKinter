import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x900+100+100")
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=18)
        self.label = tk.Label(self, text="Welcome", font=self.titlefont)
        self.label.grid(row=0, column=0)
        self.Button1 = tk.Button(self, text="Press Me", bg="green", fg="white")
        self.Button1.grid(row=1, column=0)

        self.mainloop()        

app = App()
