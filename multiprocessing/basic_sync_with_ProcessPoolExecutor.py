# Threading should be used in programs where there needs to be lot of waiting around such as IO bound tasks which involves reading/writing 
# and waiting for the read/writes (https://en.wikipedia.org/wiki/I/O_bound). Conversely, for CPU Bound tasks that involve lots of processing, 
# multiprocessing library should be used (https://en.wikipedia.org/wiki/CPU-bound).
# For I/O bound vs CPU bound explanation - https://realpython.com/python-concurrency/#when-is-concurrency-useful

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done sleeping {seconds} second(s)')

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f'Finished in {finish-start, 2} second(s)')