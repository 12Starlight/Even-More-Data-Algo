# LinkedList


class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next 
  
  def __str__(self):
    curr = self
    output = ''
    while curr:
      output += str(curr.value)
      curr = curr.next
    return output 

n = Node(1, Node(2, Node(3)))
print(n)