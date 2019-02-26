import sys
import os
from tkinter import *
import time
import datetime
import pytz
from time import gmtime
from time import *
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
    now = datetime.now()
    sys.stdout.write('\n')
    print("NYC", dt_NYC('%a %b %d, %Y: %I:%M:%S:%p '),
    print("LDN", dt_LDN('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("ZUR", dt_ZUR('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("China", dt_CNH('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("HK", dt_HK('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("Tokyo", dt_Japan('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("SYD", dt_SYD('%a %b %d, %Y: %I:%M:%S:%p '), 
    print("NZ", dt_NZ('%a %b %d, %Y: %I:%M:%S:%p '), 
    sys.stdout.flush()
    time.sleep(1)
