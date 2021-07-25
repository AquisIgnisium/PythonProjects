


import tkinter as tk
from tkinter.constants import N, X
import tkinter.messagebox
top = tkinter.Tk()

x_var = tk.StringVar()


def GetEntry():
    x = x_var.get()
    tFile = open(r"C:\Users\(put name here)\Documents\cf3.txt", "w")
    tFile.write(x + "\n")
    tFile.close()


b1 = tk.Button(text = "enter", command= GetEntry)
e1 = tk.Entry( textvariable=x_var)
e1.pack()
b1.pack()




top.mainloop()
