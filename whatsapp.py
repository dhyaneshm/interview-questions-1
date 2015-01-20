class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def buildSearchTree(arr):
  if (len(arr) == 0):
    raise Exception("Can't make a tree!")
  def recurse(arr):
    if (len(arr) == 1):
      return Node(arr[0])
    if (len(arr) == 2):
      parent = Node(arr[1])
      parent.left = Node(arr[0])
      return parent
    mid = len(arr)/2
    newNode = Node(arr[mid])
    newNode.left = recurse(arr[0:mid])
    newNode.right = recurse(arr[mid+1:])
    return newNode
  return recurse(arr)

def printTree(root):
  print "value = ", root.value
  if (root.left != None):
    print "left = ", root.left.value
    printTree(root.left)
  if (root.right != None):
    print "right = ", root.right.value
    printTree(root.right)

printTree(buildSearchTree([1,2,3,4]))