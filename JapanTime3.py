import sys
import os
from tkinter import *
import time
from time import sleep
import datetime
import pytz
from time import gmtime
from datetime import timedelta
one_hour = timedelta(hours=+1)
tz = pytz.timezone('US/Eastern')
altzone = time.altzone



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


while True:
    from datetime import datetime
    
    sys.stdout.write("\n")
                    
    print("\n", "NYC", dt_NYC.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "LDN", dt_LDN.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "ZUR", dt_ZUR.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "China", dt_CNH.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "HK", dt_HK.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "Tokyo", dt_Japan.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    print("\n", "SYD", dt_SYD.strftime('%a %b %d, %Y: %I:%M:%p '), end=' ')
    print("\n", "NZ", dt_NZ.strftime('%a %b %d, %Y: %I:%M %p '), end=' ')
    
    flush=True
    sys.stdout.flush()
    time.sleep(60)
for x in range(10):
    sys.stdout.write('\r'+str(x))
    sys.stdout.flush()


#end
