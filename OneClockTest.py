
import sys
from tkinter import *
import time
import datetime
import pytz

def tick():
  time_string = time.strftime("%a %b %d, %Y: %I:%M:%S:%p ")
  time_string1 = "London", datetime.datetime.now(tz=pytz.timezone('GMT')).strftime("%a %b %d, %Y: %I:%M:%S:%p ")
  clock.config(text=time_string)
  clock.after(200,tick)

root = Tk()
root.title("Time Zone Clock")
clock = Label(root, font = ("arial", 15, "bold"), bg= "gray")
clock.grid(row=1, column=5)
tick()
root.mainloop()


#next zone

#next zone


#end
