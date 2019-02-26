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

tstep = datetime.timedelta(seconds=1)
tnext = datetime.datetime.now() + tstep

while 1:
    
    print('\r', "NYC", dt_NYC.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')  
    
    
    print('\r', "LDN", dt_LDN.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')
    
    
    print('\r', "ZUR", dt_ZUR.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')
    
    
    print('\r', "China", dt_CNH.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n') 
    
    
    print('\r', "HK", dt_HK.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')
    
    
    print('\r', "Tokyo", dt_Japan.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')
    
    
    print('\r', "SYD", dt_SYD.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')
   
    
    print('\r', "NZ", dt_NZ.strftime('%a %b %d, %Y: %I:%M:%S:%p '), end='\n')

    tdiff = tnext - datetime.datetime.now()
    time.sleep(tdiff.total_seconds())
    tnext = tnext + tstep
    

    
#end
