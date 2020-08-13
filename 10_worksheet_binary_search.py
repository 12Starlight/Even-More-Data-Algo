'''
Binary Search Tree:
  * A tree where:
    -> The value in each node to it's left subtree is less than the current node
    -> The value in each node to it's right subtree is greater than the current 
    node

  * The reason why we use BST is so that we can have a data structure where we
  can search for values efficiently.

  * You can also perform Binary Search on a sorted array.

  * Looking up a value takes O(Log(N)), if the tree is balanced or O(h) where h
  is the height of the tree

'''


'''
Exercise 1
  Learn the basics of BTSs

  The whole point of BST is to be able to retrieve values quickly. For example,
  most implementations of ordered set data structures are actually just Binary
  Search Trees. Hence knowing how to search through a tree is vital for coding
  interviews. If you mess that up, you might get automatically rejected. The 
  data structure of a Tree usually looks like this:

    class TreeNode:
      def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None

  Solve all the following questions in your preferred language.

'''

# Search in a Binary Search Tree

# Insert into a Binary Search Tree

# Delete Node in BST


'''
Exercise 2
  Applying BST strategies

  The following questions are a bit more difficult. It requires a bit more
  creativity, but you have everything you need to solve it. Try to solve the
  question using BST and time yourself. 

'''

# Kth Largest Element In A Stream

