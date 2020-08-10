class Node(object):
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

  # Pre Order Recursive
  def preorder(self):
    print(self.value)
    for child in self.children:
      child.preorder() 

  # Pre Order Iterative
  def preorderIter(self):
    stack = [self]
    while len(stack):
      node = stack.pop()
      print(node.value)
      for child in reversed(node.children):
        stack.append(child)

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

root.preorder()
# abdecf
print('')

root.postorder()
# debfca

print('')
root.preorderIter()
# abdecf