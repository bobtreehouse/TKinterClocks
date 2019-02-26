
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

###MAIN 4 zones only ==>check 
## *this is clock number 1 below; down to double hash ##
# only NYC clock below updates in seconds; 1000=milliseconds  = 1 second
def tick():
  time_string = time.strftime("%a %b %d, %Y: %I:%M:%S:%p")
  clock.config(text=time_string)
  clock.after(1000,tick)
  
##remove hash for clock after but burns CPU
# all other time zones update to the minute so 60000 milliseconds = 1 minute
  

  time_string_1 = datetime.datetime.now(tz=pytz.timezone('Europe/London')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  clock_1.config(text=time_string_1)
  clock_1.after(60000,tick)
  
#3 (off)
  #time_string_2 = datetime.datetime.now(tz=pytz.timezone('Europe/Zurich')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  #clock_2.config(text=time_string_2)
  #clock_2.after(60000,tick)

#4
  time_string_3 = datetime.datetime.now(tz=pytz.timezone('Japan')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  clock_3.config(text=time_string_3)
  clock_3.after(60000,tick)

#5 (off)
  #time_string_4 = datetime.datetime.now(tz=pytz.timezone('Hongkong')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  #clock_4.config(text=time_string_4)
  #clock_4.after(60000,tick)

#6
  time_string_5 = datetime.datetime.now(tz=pytz.timezone('Australia/Sydney')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  clock_5.config(text=time_string_5)
  clock_5.after(60000,tick)

#7 (off)
  #time_string_6 = datetime.datetime.now(tz=pytz.timezone('NZ')).strftime(" %a %b %d, %Y: %I:%M %p ")  
  #clock_6.config(text=time_string_6)
  #clock_6.after(60000,tick)


root = Tk()
root.title("FX Time Zones")
#clock 1 just here:
label_0 = Label(root, text="NYC", font = ("arial", 14, "bold"), bg= "gray", fg="black")
label_0.grid(row=0, column=0, sticky=EW)
clock = Label(root, font = ("arial", 14, "bold"), bg= "gray")
clock.grid(row=1, column=0)
  

#clock 2 is below:
label_1 = Label(root, text="London", font = ("arial", 14, "bold"), bg= "gray", fg="black")
label_1.grid(row=0, column=1, sticky=EW)
clock_1 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
clock_1.grid(row=1, column=1)

#clock 3 is below: (off)
#label_2 = Label(root, text="Zurich", font = ("arial", 14, "bold"), bg= "gray", fg="black")
#label_2.grid(row=0, column=2, sticky=EW)
#clock_2 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
#clock_2.grid(row=1, column=2)

#clock 4 is below:
## grid repositioned ! 
label_3 = Label(root, text="Tokyo", font = ("arial", 14, "bold"), bg= "gray", fg="black")
label_3.grid(row=0, column=2, sticky=EW)
clock_3 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
clock_3.grid(row=1, column=2)

#clock 5 is below: (off)
#label_4 = Label(root, text="Hong Kong", font = ("arial", 14, "bold"), bg= "gray", fg="black")
#label_4.grid(row=0, column=4, sticky=EW)
#clock_4 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
#clock_4.grid(row=1, column=4)

#clock 6 is below:
## grid repositioned ! 
label_5 = Label(root, text="Sydney", font = ("arial", 14, "bold"), bg= "gray", fg="black")
label_5.grid(row=0, column=3, sticky=EW)
clock_5 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
clock_5.grid(row=1, column=3)

#clock 7 is below: (off)
#label_6 = Label(root, text="Auckland", font = ("arial", 14, "bold"), bg= "gray", fg="black")
#label_6.grid(row=0, column=6, sticky=EW)
#clock_6 = Label(root, font = ("arial", 14, "bold"), bg= "gray")
#clock_6.grid(row=1, column=6)


#flush=True
tick()
root.mainloop()










##components above make the whole clock

#question is does clock two go up above here 
