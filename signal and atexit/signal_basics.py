
# https://www.askpython.com/python-modules/python-signal
# https://docs.python.org/3/library/signal.html

import signal
import time  
 
# Our signal handler
def signal_handler(signum, frame):  
    print("Signal Number:", signum, " Frame: ", frame)  
 
def exit_handler(signum, frame):
    print('Exiting....')
    exit(0)

if __name__=="__main__": 
    # Register our signal handler with `SIGINT`(CTRL + C)
    signal.signal(signal.SIGINT, signal_handler)
    
    # Register the exit handler with `SIGTSTP` (Ctrl + Z)
    signal.signal(signal.SIGTSTP, exit_handler)
    
    # While Loop
    while 1:  
        print("Press Ctrl + C") 
        time.sleep(3) 