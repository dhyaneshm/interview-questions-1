triangle = """
   3
  7 4
 2 4 6
8 5 9 3
"""

'''
1. process the string and create a tree of nodes
2. start at the root node and have a recursive algorithm that returns themax Sum
3. (potentially optimize with cache memorization)
'''

class Node:
    def __init__(self, value, parent):
        self.value = int(value)
        self.left = None
        self.right = None
        self.parent = parent

def buildTree(triangle):
  #need to build the root!
    rows = triangle.strip().split('\n')
    root = Node(row[0].strip(), None)
    parents = [root]
    
    for row in rows[1:]:
        rowVals = row.strip().split(' ')
        newParents = []
        for i in range(len(rowVals)):
            if (i%2 == 1):
                continue
            parent = parents.pop(0)
            leftChild = Node(rowVals[i], parent) #left child
            rightChild = Node(rowVals[i+1], parent) 
            parent.left = leftChild
            parent.right = rightChild
            newParents.append(leftChild)
            newParents.append(rightChild)
        parents = newParents
    return root
          
root = buildTree(triangle)

def maxSum(root):
    cache = {}
    def recurse(cur):
        if cur == None:
            return 0
        if cur in cache:
            return cache[cur]
        return max(recurse(cur.left)+cur.value, recurse(cur.right)+cur.value)
    return recurse(root)

print maxSum(root)