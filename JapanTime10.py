from __future__ import print_function
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


print('\r',"NYC", dt_NYC.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"LDN", dt_LDN.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"ZUR", dt_ZUR.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"China", dt_CNH.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"HK", dt_HK.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"Tokyo", dt_Japan.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"SYD", dt_SYD.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True)
print('\r',"NZ", dt_NZ.current_time('%a %b %d, %Y: %I:%M:%S:%p '), end='\r', flush=True))
    
time.sleep(1)


