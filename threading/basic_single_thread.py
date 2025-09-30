# https://realpython.com/intro-to-python-threading/#starting-a-thread

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    
    # https://realpython.com/intro-to-python-threading/#daemon-threads
    # A daemon is a process that runs in the background. A daemon thread will shut down immediately when the program exits. 
    # If a program is running Threads that are not daemons, then the program will wait for those threads to complete before 
    # it terminates. Threads that are daemons, however, are just killed wherever they are when the program is exiting.
    # 
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # To tell one thread to wait for another thread to finish, you call .join(). If you uncomment the below line, the main 
    # thread will pause and wait for the thread x to complete running.
    #
    # x.join()
    logging.info("Main    : all done")