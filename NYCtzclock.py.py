
import sys
from tkinter import *
import time

def tick():
  time_string = time.strftime("%a %b %d, %Y: %I:%M:%S:%p %Z")
  clock.config(text=time_string)
  clock.after(200,tick)

root = Tk()
clock = Label(root, font = ("arial", 15, "bold"), bg= "gray")
clock.grid(row=1, column=1)
tick()
root.mainloop()
