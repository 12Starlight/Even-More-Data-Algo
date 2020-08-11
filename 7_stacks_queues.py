'''
  Stack: LIFO (Last In First Out)
    * push()
    * pop()
    * peek()

  Queue: FIFO (First In First Out)
    * push()/enqueue()
    * pop()/dequeue()
    * peek()

'''


# Create Stack
s = [];
s.append(1)
s.append(2)
s.append(3)
print(s)

# Peek (ref the -1 index, traverse from the end of the array, gets last elm)
print(s[-1])

# Get reverse values in the order the came in
print(s.pop())
print(s.pop())
print(s.pop())


# Create Queue
from queue import deque

q = deque
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
print(q)