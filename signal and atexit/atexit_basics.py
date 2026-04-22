# https://docs.python.org/3/library/atexit.html

# Example - https://docs.python.org/3/library/atexit.html#atexit-example

def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')