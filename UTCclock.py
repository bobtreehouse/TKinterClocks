
import sys
import os
from tkinter import *
import time
import datetime
import pytz
from time import gmtime
from datetime import timedelta
one_hour = timedelta(hours=+1)
tz = pytz.timezone('US/Eastern')
altzone = time.altzone

def tick():
  time_string1 = datetime.datetime.now(tz=pytz.timezone('UTC')).strftime("%a %b %d, %Y: %I:%M:%S %p ")
  clock.config(text=time_string1)
  clock.after(1000,tick)

root = Tk()
root.title("UTC")
clock = Label(root, font = ("arial", 14, "bold"), bg= "gray")
clock.grid(row=1, column=1)
tick()
root.mainloop()
