# https://realpython.com/intro-to-python-threading/#producer-consumer-using-queue

# The "threading.Event" object allows one thread to signal an event while many other threads can be waiting for that "event" to happen.
# The threads that are waiting for the event do not necessarily need to stop what they are doing, they can just check the status of the
# "Event" every once in a while.

import random
import logging
import threading
import concurrent.futures
import time
import queue

def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )

    logging.info("Consumer received EXIT event. Exiting")

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        value = self.get()
        logging.debug("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s:added %d to queue", name, value)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()

# If you read through the output in this example, you can see some interesting things happening. Right at the top, you can see the 
# producer got to create five messages and place four of them on the queue. It got swapped out by the operating system before it 
# could place the fifth one.

# The consumer then ran and pulled off the first message. It printed out that message as well as how deep the queue was at that point
# given below:
# Consumer storing message: 32 (queue size=3)

# This is how you know that the fifth message hasn’t made it into the pipeline yet. The queue is down to size three after a single 
# message was removed. You also know that the queue can hold ten messages, so the producer thread didn’t get blocked by the queue. 
# It was swapped out by the OS.

# Note: Your output will be different. Your output will change from run to run. That’s the fun part of working with threads!

# As the program starts to wrap up, can you see the main thread generating the event which causes the producer to exit immediately. T
# he consumer still has a bunch of work do to, so it keeps running until it has cleaned out the pipeline