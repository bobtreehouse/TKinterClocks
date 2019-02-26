
import sys
from tkinter import *
import time
import datetime
import pytz

def tick():
  time_string1 = "AUS", datetime.datetime.now(tz=pytz.timezone('Australia/Sydney')).strftime("%a %b %d, %Y: %I:%M:%S:%p ")
  clock.config(text=time_string1)
  clock.after(200,tick)


root = Tk()
clock = Label(root, text=" ", font = ("arial", 15, "bold"), bg= "gray")
clock.grid(row=2, column=1)
tick()
root.mainloop()
