import tkinter as tk
from tkinter import font as tkFont

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x800+0+0")
        self.titlefont = tkFont.Font(family="Arial", size=30, slant="italic")

        # ust a title label
        l0 = tk.Label(text="Graph App", bg="#ffaaaa", font=self.titlefont)
        l0.grid(row=0,column=0, columnspan=4, sticky="NSEW")

        # Another little label
        l1 = tk.Label(text="Enter values below:" )
        l1.grid(row=1, column=0)

        # The entry box for typing in numbers
        self.entry = tk.Entry(width=30)
        self.entry.grid(row=2, column=0)

        # A submit button
        b1 =tk.Button(text="Add", command = self.add)
        b1.grid(row=2, column=1)

        # The canvas for drawing the graph
        self.theCanvas = tk.Canvas(self,width=800, height=400, bg="#ddddff")
        self.theCanvas.grid(row=3, column=3)
        
        # A list of numbers to go into the graph
        self.list = tk.Listbox(width=20, height=20)
        self.list.grid(row=3, column=0)

        # Some formatting to make the columns fit
        self.columnconfigure(2,minsize=100)
        self.columnconfigure(3,weight=1)
        
        self.bind("<Return>", self.add)

        self.drawgraph()
        self.mainloop()


    def drawgraph(self):
        self.theCanvas.delete(tk.ALL) # clears the canvas
        self.theCanvas.create_line(750,350,50,350,fill="black")
        self.theCanvas.create_line(50,350,50,50,fill="black")# draws a line from x,y (700,50) to (0,350) 
                
        numvals = self.list.get(0, tk.END)
        biggestNum = 0
        for num in numvals:
            if int(num) > biggestNum:
                biggestNum = int(num)
                
        boxAmt = len(numvals)
        i=0
        for num in numvals:
            x1 = 50+(700/boxAmt)*i
            x2 = x1 + (700/boxAmt) - 5
            
            if biggestNum > 350:
                self.theCanvas.create_rectangle(x1,350,x2,350- (int(num) / biggestNum)*300, fill="red")
            else:
                self.theCanvas.create_rectangle(x1,350,x2,350-int(num), fill="red")
            i += 1


  
            
    def add(self):
        # this should add the number in the entry box into the listbox
        # it should only accept numerical values
        
        text = self.entry.get()
        
        if int(text.isnumeric()):
            self.list.insert(tk.END, text)
            
        self.entry.delete(0,tk.END)

        self.drawgraph()

app = Main()


        