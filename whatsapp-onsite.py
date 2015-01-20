
alreadySeen = {}
def deepCopy(root):
  if (root == None):
    raise Exception("can't clone empty node")
  cloneRoot = Node.newA() if root.getType() == A else Node.newB()
  duplicate(root, cloneRoot)
  alreadySeen[root] = cloneRoot
  return cloneRoot

# add clones of origNode's children to cloneNode
def duplicate(origNode, cloneNode):
  for child in origNode.getChildren():
    newNode = None
    if (child in alreadySeen):
      newNode = alreadySeen[child]
    else:
      newNode = Node.newA() if child.getType() == A else Node.newB()
    cloneNode.addChild(newNode)
    if child not in alreadySeen:
      alreadySeen[child] = newNode
      duplicate(child, newNode)