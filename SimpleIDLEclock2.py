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
from time import strftime


dt_Japan = datetime.datetime.now(tz=pytz.timezone('Japan'))
dt_UCT = datetime.datetime.now(tz=pytz.timezone('UCT'))
dt_NYC = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
dt_GMT = datetime.datetime.now(tz=pytz.timezone('GMT'))
dt_LDN = datetime.datetime.now(tz=pytz.timezone('Europe/London'))
dt_NZ = datetime.datetime.now(tz=pytz.timezone('NZ'))
dt_SYD = datetime.datetime.now(tz=pytz.timezone('Australia/Sydney'))
dt_HK = datetime.datetime.now(tz=pytz.timezone('Hongkong'))
dt_CNH = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))
dt_ZUR = datetime.datetime.now(tz=pytz.timezone('Europe/Zurich'))


x=1;
while (x==1 ):
    current_time=datetime.datetime.now().strftime("NYC %a %b %d, %Y: %I:%M:%S:%p ")
    time_string1 = "AUS", datetime.datetime.now(tz=pytz.timezone('Australia/Sydney')).strftime("%a %b %d, %Y: %I:%M:%S:%p ")
    clock=(time_string1)
    clock.after=(200,tick)
    print(clock)
      

end='\r'
#end
