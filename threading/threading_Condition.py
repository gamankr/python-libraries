# CONDITION - https://medium.com/@shashikantrbl123/understanding-condition-variables-in-python-for-thread-synchronization-329a166dfc9e
# https://stackoverflow.com/questions/7424590/threading-condition-vs-threading-event
# https://docs.python.org/3/library/threading.html#condition-objects

# ****Key concepts related to condition variables****

# Wait: The wait() method is used by a thread to block its execution and wait until it is notified. The thread releases any associated 
# lock or resource while waiting.

# Notify: The notify() method is used to wake up a single waiting thread that is blocked on the condition variable. It informs the 
# waiting thread that the condition has changed, allowing it to recheck the condition and continue its execution.

# NotifyAll: The notifyAll() method is used to wake up all the waiting threads that are blocked on the condition variable. It notifies 
# them that the condition has changed, and they can recheck the condition to determine if they can proceed.

import threading

# Shared resource
shared_resource: list = []

# Condition variable
condition = threading.Condition()

# Consumer thread
def consumer():
    with condition:
        while not shared_resource:
            print("Consumer is waiting...")
            condition.wait()
        item = shared_resource.pop(0)
        print("Consumer consumed item:", item)

# Producer thread
def producer():
    with condition:
        item = "New item"
        shared_resource.append(item)
        print("Producer produced item:", item)
        condition.notify()


if __name__ == "__main__":
    # Create and start the threads
    consumer_thread = threading.Thread(target=consumer)
    producer_thread = threading.Thread(target=producer)
    consumer_thread.start()
    producer_thread.start()

#Output
'''
Producer produced item: New Item
Consumer consumed item: New Item
'''