'''
Binary Search Tree:
  -> Sorted
  -> Data in Nodes
  -> 2 Branch

  Avg: O(Log(N))
  Worst: O(N) (list of nodes going down one branch)

  
  Graph
    V
  Tree
    V
  Binary Tree
    V
  Binary Search Tree

'''


# Create Binary Search Tree
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

#        4
#      /   \
#     2     6
#    / \     \
#   1   3     7

node = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))