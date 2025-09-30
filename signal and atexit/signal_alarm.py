# https://www.askpython.com/python-modules/python-signal

import signal  
import time  
 
def alarm_handler(signum, frame):  
    print('Alarm at:', time.ctime())  
 
# Register the alarm signal with our handler
signal.signal(signal.SIGALRM, alarm_handler)
 
signal.alarm(3)  # Set the alarm after 3 seconds  
 
print('Current time:', time.ctime())  
 
time.sleep(6)  # Make a sufficient delay for the alarm to happen 