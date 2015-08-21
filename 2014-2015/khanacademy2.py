# We have a tree that is stored as a list, with each node storing
# the IDs of its children, for example:

node_tree = [
    { "id": "root",  "children": [ "b", "a", "h" ] },
    { "id": "a",     "children": [ "c", "d" ] },
    { "id": "c",     "children": [ "f" ] },
    { "id": "b",     "children": [ "e" ] },
    { "id": "d",     "children": [ "g" ] },
    { "id": "e",     "children": [] },
    { "id": "f",     "children": [] },
    { "id": "g",     "children": [] },
    { "id": "h",     "children": [] },
]

# Write a function that moves a node identified by id (and it’s subtree) from one specified parent to another at a specified index.

1. moveNode("d", "a", "b", 0, nodeTree) => Success!
2. moveNode("root", "", "a", 0, nodeTree) => raise exception about cycle
3. moveNode("d", "a", "b", 3, nodeTree)  => out of index
4. moveNode("a", "root", "root", 2, nodeTree)  => should succeed
5. moveNode("a", "g", "root", 2, nodeTree)  => should not succeed
6. moveNode("a", "root", "x", 0, nodeTree) => should not succeed
7. moveNode("a", "root", "c", 0, nodeTree) => should raise exception about cycle
8. moveNode("a", "root", "a", 0, nodeTree) => should raise exception about cycle

#c an't move into descendents or itself!
class Node:
  def __init__(self, id):
    self.id = id
    self.children = []
  
def getNode(nodeTree, targetId):
  for i, node in enumerate(nodeTree):
    if node.id == targetId:
      return node
  return None
  
def getDescendents(nodeTree, curNode):
  descendents = set()
  def recurse(nodeTree, curNode):
    for childId in curNode.children:
      descendents.add(childId)
      recurse(nodeTree, getNode(nodeTree, childId))
  recurse(nodeTree, curNode)
  return descendents

def moveNode(curId, oldParentId, newParentId, index, nodeTree):
  curNode = getNode(nodeTree, curId)
  oldParentNode = getNode(nodeTree, oldParentId)
  newParentNode = getNode(nodeTree, newParentId)
  if curNode == None or oldParentNode == None or newParentNode == None:
    raise Exception ("Node doesn't exist!")
  # Catches if oldParentNode doesn't contain current Node that is to be moved
  if (curId not in oldParentNode.children):
    raise Exception ("invalid old parent Id")
  # newParentNode can't be curNode or any of curNode's descents  
  descendents = getDescendents(nodeTree, curNode)
  
  if newParentNode.id in descendents or newParentNode == curNode:
    raise Exception("Cycle! bad news!")
  if (index < 0 or index > len(newParentNode.children)):
    raise Exception("invalid index to insert!")
    
  #remove curNode from oldParent and add to new parent
  oldParentNode.children.remove(curId) #O(n)
  newParentNode.children.insert(index, curId)
  
  
  
  
  
  
  
  
  