import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x900+100+100")
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=18)
        self.label = tk.Label(self, text="hi welcome hi yes hello welcome app", font=self.titlefont)
        self.label.grid(row=0, column=0, columnspan=2)
        self.Button1 = tk.Button(self, text="Press Me", bg="green", fg="white", command=self.buttonPressed)
        self.Button1.grid(row=2, column=1)
        self.label2 = tk.Label(self, text="AAHHHGHAHH AHGH HAHH", font=self.titlefont)
        self.label2.grid(row=3, column=0, sticky="EW", columnspan = 2)
        
        self.textBox = tk.Entry(self, text="type type type", font=self.titlefont, show="*")
        self.textBox.grid(row=2,column=0)
        self.textBox.bind("<Return>", self.buttonPressed)

        self.mainloop()
        
    def buttonPressed(self, e=None):
        if self.textBox.get() == "banana":
            self.label2.config(text="good", bg="green")
        else:
            self.label2.config(text="perish", bg="red")

app = App()