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

  You are basically inserting N elements into a Binary Search Tree that is of 
  H (height) Log(N), and you just traverse through the height of that Binary
  Tree and find the position to insert it and add it there, and repeatedly you do
  so.

  So you can imagine that the time complexity of building a Binary Search Tree
  is N * Log(N). And that makes sense, bc if you think about it, the fastest 
  sort algorithm that we have is also N * Log(N) time and Binary Search Trees,
  essentially sort all of the elments.

  So, if there was possibly a faster way to build a Binary Search Tree, then you
  would essentually have a faster sort algorithm than, N * Log(N) which gives us
  a hint that the fastest way we can construct a Binary Search Tree is 
  N * Log(N). 

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

# In Order
def inorder(node):
  if not node:
    return
  inorder(node.left)
  print(node.val)
  inorder(node.right)

inorder(node)
print('')

# Pre Order
def preorder(node):
  if not node:
    return
  print(node.val)
  preorder(node.left)
  preorder(node.right)

preorder(node)
print('')

# Search
def search(node, key):  
  if not node:
    return None 
  if node.val == key: 
    return node 
  if key > node.val: 
    return search(node.right, key)
  else: 
    return search(node.left, key)

print(search(node, 6).val) # 6
print(search(node, 57)) # None
print('')

# Binary Search
def binarySearch(nums, low, high, x):
  if high < low:
    return None 
  mid = (low + high) // 2
  if nums[mid] == x:
    return mid 
  elif nums[mid] > x:
    return binarySearch(nums, low, mid - 1, x)
  else:
    return binarySearch(nums, mid + 1, high, x)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(nums, 0, len(nums) - 1, 4)) # 3
print(binarySearch(nums, 0, len(nums) - 1, 40)) # None