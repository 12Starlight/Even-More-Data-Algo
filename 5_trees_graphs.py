class Node(object):
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

  # Pre Order Recursive
  def preorder(self):
    print(self.value)
    for child in self.children:
      child.preorder() 

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
print("")

root.postorder()
# debfca