from queue import deque

class Node(object):
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

  # Pre Order Recursive
  def dfspreorder(self):
    print(self.value)
    for child in self.children:
      child.preorder() 

  # Pre Order Iterative (Stack)
  def dfspreorderIter(self):
    stack = [self]
    while len(stack):
      node = stack.pop()
      print(node.value)
      for child in reversed(node.children):
        stack.append(child)

  # Pre order Iterative (Queue)
  def bfspreorderIter(self):
    queue = deque([self])
    while len(queue):
      node = queue.popLeft()
      print([node.value])
      for child in node.children:
        queue.append(child)

  # Post Order Recursive
  def postorder(self):
    for child in self.children:
      child.postorder()
    print(self.value)

  
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f


root = Node('a', [Node('b', [Node('d'), Node('e')]), Node('c', [Node('f')])])

root.dfspreorder()
# abdecf
print('')

root.postorder()
# debfca

print('')
root.dfspreorderIter()
# abdecf

print('')
root.bfspreorderIter()
# abdecf