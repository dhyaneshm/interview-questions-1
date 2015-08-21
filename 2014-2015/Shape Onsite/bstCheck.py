# Write a function to verify if you have a binary search tree


"""
BST Node Class
"""
class Node:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

  def __repr__(self):
    return "NODE: val = "+str(self.value)+"\nLEFT: "+str(self.left)+"\nRIGHT: "+str(self.right)

class BST:
  def __init__(self):
    self.root = None

  def add(self, value):
    newNode = Node(value)
    if self.root == None:
      self.root = newNode
      return
    cur = self.root
    parent = None
    left = False
    while (cur != None):
      parent = cur
      if value < cur.value:
        cur = cur.left
        left = True
      else:
        cur = cur.right
        left = False
    if left: 
      parent.left = newNode
    else: 
      parent.right = newNode

"""
Method: isBST
--------------------------
Parameters: root - the root of the specified BST represented as a BST node
Returns: True or False depending on whether the specified BST is valid or not
--------------------------
"""
def isBST(root):
  def recurse(cur, low, high):
    if cur == None: return True
    left = False
    right = False
    if cur.value > low and cur.value < high:
      left = recurse(cur.left, low, cur.value)
      right = recurse(cur.right, cur.value, high)
      return (left and right)
    else: 
      return False
  return recurse(root, float("-inf"), float("inf"))

"""
Method: printTree
A rudimentary method of printing the tree level by level
--------------------------
Parameters: root - the root of the specified BST represented as a BST node
Returns: N/A
--------------------------
"""
def printTree(root):
  thislevel = [root]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print n.value,
      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
    print
    thislevel = nextlevel

"""
Simple testing framework to create a tree and then test its validity
"""
tree = BST()
tree.add(5)
tree.add(8)
tree.add(6)
tree.add(1)
tree.add(9)
tree.add(10)
tree.add(-2)
tree.add(12)
tree.add(7)

# make tree invalid
tree.root.right.right.value = -2

print isBST(tree.root)


