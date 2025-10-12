# Corey Schafer threading video - https://www.youtube.com/watch?v=IEEhzQoKtQU

import time
import concurrent.futures
     

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds} second(s)'

start = time.perf_counter() 

# ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
# All threads enqueued to ThreadPoolExecutor will be "joined" before the interpreter can exit.
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) # submit() method returns a "Future" object which represents 
                                          # the result of an asynchronous computation. submit() method 
                                          # submits each function one at a time
    print(f1.result())

finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} second(s)')

start = time.perf_counter()  

# starting 10 threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)] 
    # results is a list of Future objects

    # If you don't use as_completed, results are printed in the order the threads were submitted 
    # instead of completion. Check next block for further testing
    for future in concurrent.futures.as_completed(results):
        print(future.result())

finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} second(s)')

start = time.perf_counter()  

# starting 5 threads with different sleep times
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]   
    # results is a list of Future objects

    # Output WITHOUT concurrent.futures.as_completed() - in order of thread submission
    # Done Sleeping...5 second(s)
    # Done Sleeping...4 second(s)
    # Done Sleeping...3 second(s)
    # Done Sleeping...2 second(s)
    # Done Sleeping...1 second(s)
    for future in results:
        print(future.result())

    # Output WITH concurrent.futures.as_completed() - in order of thread completion
    # Done Sleeping...1 second(s)
    # Done Sleeping...2 second(s)
    # Done Sleeping...3 second(s)
    # Done Sleeping...4 second(s)
    # Done Sleeping...5 second(s)
    for future in concurrent.futures.as_completed(results):
        print(future.result())

finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} second(s)')

start = time.perf_counter()  

# using map() instead of submit()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    executor.map(do_something, secs) # arguments are the function and an iterable (here, a list) 
                                     # containing the arguments to the function


finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} second(s)')