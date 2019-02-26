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


dt_Japan = datetime.now(tz=pytz.timezone('Japan'))
dt_UCT = datetime.now(tz=pytz.timezone('UCT'))
dt_NYC = datetime.now(tz=pytz.timezone('US/Eastern'))
dt_GMT = datetime.now(tz=pytz.timezone('GMT'))
dt_LDN = datetime.now(tz=pytz.timezone('Europe/London'))
dt_NZ = datetime.now(tz=pytz.timezone('NZ'))
dt_SYD = datetime.now(tz=pytz.timezone('Australia/Sydney'))
dt_HK = datetime.now(tz=pytz.timezone('Hongkong'))
dt_CNH = datetime.now(tz=pytz.timezone('Asia/Shanghai'))
dt_ZUR = datetime.now(tz=pytz.timezone('Europe/Zurich'))

while True:
        
        print("NYC", dt_NYC.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("LDN", dt_LDN.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("ZUR", dt_ZUR.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("China", dt_CNH.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("HK", dt_HK.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("Tokyo", dt_Japan.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("SYD", dt_SYD.strftime('%a %b %d, %Y: %I:%M:%S:%p '))
        print("NZ", dt_NZ.strftime('%a %b %d, %Y: %I:%M:%S:%p '))

sys.stdout.flush()
print("\r"),
time.sleep(1)
      

#end
