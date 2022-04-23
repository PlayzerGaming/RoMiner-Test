import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import tkinter.messagebox
import random
import sys, string, os



root = tk.Tk()
new = 1
url = "http://rominer.online"


root.geometry("525x285")
root.title('RoMiner Robux Miner (Made by Playzer#7447)') #title at the top of the prorgam
# Canvas work below, dont change
Canvas = tk.Canvas(root, height=285, width=525, bg="#000000") #code for the frame to be there, dont change
Canvas.create_text(250, 15, text="Welcome to RoMiner. The Robux crypto miner.", fill="white", font=('Impact')) # top text lol
Canvas.place(x=-2, y=0)
root.resizable(False, False) #determines if the program is resizable or not
def openweb():
    webbrowser.open(url, new=new)

open1 = open("mine_eth.bat")


btn = tkinter.Button(Canvas, text="Open Website", command=openweb, bg="Gray", fg="White", activebackground="Gray", activeforeground="White", font="Impact")
btn2 = tkinter.Button(Canvas, text="Start Mining!", command=open1, bg="Gray", fg="White", activebackground="Gray", activeforeground="White", font="Impact")
btn.place(x=10, y=50)
btn2.place(x=10, y=220)






root.mainloop()