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

while True:
    
    print(("NYC", dt_NYC.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print'/n', flush=False))
    print(("LDN", dt_LDN.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("ZUR", dt_ZUR.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("China", dt_CNH.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("HK", dt_HK.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("Tokyo", dt_Japan.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("SYD", dt_SYD.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))
    print(("NZ", dt_NZ.strftime('%a %b %d, %Y: %I:%M:%S:%p '), print='/n', flush=False))

time.sleep(1)
      

#end
