# FIFO queue - First In First Out

from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        self._elements.popleft()
    
    def __len__(self):
        return len(self._elements)
    
    def __repr__(self):
        return repr(self._elements)
    
lifo = Queue("1st", "2nd", "3rd")
print(len(lifo))

lifo.enqueue("4th")
print(lifo)

lifo.dequeue()
print(lifo)

    

