import tkinter as tk
from tkinter import font as tkFont
import random

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x900+100+100")
        self.defaultFont = tkFont.Font(family="Arial", size=50, slant="italic")
        
        self.currentNumber = ""
        self.total = 0
        self.operation = "add"
        self.opReady = False
        
        self.columnconfigure(0, weight=100)
        self.columnconfigure(1, weight=100)
        self.columnconfigure(2, weight=100)
        self.rowconfigure(0, weight=100)
        self.rowconfigure(1, weight=100)
        self.rowconfigure(2, weight=100)
        self.rowconfigure(3, weight=100)
        self.rowconfigure(4, weight=100)
        self.rowconfigure(5, weight=100)
        

        
        self.output = tk.Label(self, font=self.defaultFont, text="placeholder", bg="white")
        self.output.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=5, sticky="NEWS", pady=50, padx=50)
        
        self.button1 = tk.Button(self, font=self.defaultFont, text="1", bg="grey", fg="white", command = lambda: self.digitPressed(1))
        self.button1.grid(row=1,column=0, sticky="NEWS")
        
        self.button2 = tk.Button(self, font=self.defaultFont, text="2", bg="grey", fg="white", command = lambda: self.digitPressed(2))
        self.button2.grid(row=1,column=1,sticky="NEWS")
        
        self.button3 = tk.Button(self, font=self.defaultFont, text="3", bg="grey", fg="white", command = lambda: self.digitPressed(3))
        self.button3.grid(row=1,column=2,sticky="NEWS")
        
        self.button4 = tk.Button(self, font=self.defaultFont, text="4", bg="grey", fg="white", command = lambda: self.digitPressed(4))
        self.button4.grid(row=2,column=0,sticky="NEWS")
        
        self.button5 = tk.Button(self, font=self.defaultFont, text="5", bg="grey", fg="white", command = lambda: self.digitPressed(5))
        self.button5.grid(row=2,column=1,sticky="NEWS")
        
        self.button6 = tk.Button(self, font=self.defaultFont, text="6", bg="grey", fg="white", command = lambda: self.digitPressed(6))
        self.button6.grid(row=2,column=2,sticky="NEWS")
        
        self.button7 = tk.Button(self, font=self.defaultFont, text="7", bg="grey", fg="white", command = lambda: self.digitPressed(7))
        self.button7.grid(row=3,column=0,sticky="NEWS")
        
        self.button8 = tk.Button(self, font=self.defaultFont, text="8", bg="grey", fg="white", command = lambda: self.digitPressed(8))
        self.button8.grid(row=3,column=1,sticky="NEWS")
        
        self.button9 = tk.Button(self, font=self.defaultFont, text="9", bg="grey", fg="white", command = lambda: self.digitPressed(9))
        self.button9.grid(row=3,column=2,sticky="NEWS")
        
        self.button0 = tk.Button(self, font=self.defaultFont, text="0", bg="grey", fg="white", command = lambda: self.digitPressed(0))
        self.button0.grid(row=4,column=1,sticky="NEWS")
        
        self.add = tk.Button(self, font=self.defaultFont, text="+", bg="#B2F7D9", fg="white")
        self.add.grid(row=5,column=0,sticky="NEWS")
        
        self.subtract = tk.Button(self, font=self.defaultFont, text="-", bg="#FF82B4", fg="white")
        self.subtract.grid(row=5,column=1,sticky="NEWS")
        
        self.equals = tk.Button(self, font=self.defaultFont, text="=", bg="#CCEBEB", fg="white")
        self.equals.grid(row=5,column=2,sticky="NEWS")
        
        self.mainloop()
    
    def digitPressed(self, num):
        self.currentNumber += str(num)
        self.output.config(text=self.currentNumber)
        
    def plusPressed(self):
        
        if opReady:
            if self.operation == "add":
                self.total
        
        self.operation = "add"
        self.total += int(self.currentNumber)
        self.currentNumber = ""
        self.opReady = True
    def subtractPressed(self):
        #awhbfaAWJ JHF JAU AGJ AWJVF
        self.operation = "subtract"
        self.total += int(self.currentNumber)
        self.currentNumber = ""
        
    def equalsPressed(self):
        pass
    
        
app = App()