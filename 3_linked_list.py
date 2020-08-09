# LinkedList

'''
  Linked Lists are usually a list of nodes. And each node has a 'Value' and a
  'Next' where 'Next stores the address of the next node. That is how they can
  be chained together. So a whole Linked List is essentially just chained up
  Nodes
  
'''


# Create Node 
class Node(object):
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next 
    # Doubly LinkedList
      # Then assign to prior pointers 
    self.prev = prev
  
  # override _str_(self) to print values
  def __str__(self):
    curr = self
    output = ''
    while curr:
      output += str(curr.value)
      curr = curr.next
    return output 

n = Node(1, Node(2, Node(3)))
print(n)


# Convert Array To LinkedList
def list2LinkedList(nums):
  head = None 
  curr = None 
  for n in nums:
    if not head:
      head = Node(n)
      curr = head 
    else: 
      curr.next = Node(n)
      curr = curr.next
  return head

print(list2LinkedList([10, 20, 30]))