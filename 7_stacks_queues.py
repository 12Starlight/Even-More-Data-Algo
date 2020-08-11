'''
  Stack: LIFO (Last In First Out)
    * push()  O(1) Time | O(N) Space
    * pop()  O(1) Time | O(N) Space
    * peek()  O(1) Time | O(N) Space

  Queue: FIFO (First In First Out)
    * push()/enqueue()  O(1) Time | O(N) Space
    * pop()/dequeue()  O(1) Time | O(N) Space
    * peek()  O(1) Time | O(N) Space

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
from collections import deque

q = deque()
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
print(q)

# Peek (ref the -1 index, traverse from the end of the array, gets last elm)
print(q[-1])

# Get reverse values in the order the came in
print(q.pop())
print(q.pop())
print(q.pop())