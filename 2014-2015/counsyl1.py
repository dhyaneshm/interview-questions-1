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
    def __init__(self, value):
        self.value = int(value)
        self.left = None
        self.right = None

def buildTree(triangle):
  #need to build the root!
    rows = triangle.strip().split('\n')
    root = Node(rows[0].strip())
    parents = [root]
    
    for row in rows[1:]:
        rowVals = row.strip().split(' ')

        firstChild = Node(rowVals[0])
        parents[0].left = firstChild
        lastChild = Node(rowVals[-1])
        parents[-1].right = lastChild
        newParents = [firstChild]

        for i in range(1, len(rowVals)-1):
            leftParent = parents[i-1]
            rightParent = parents[i]
            newNode = Node(rowVals[i])
            leftParent.right = newNode
            rightParent.left = newNode
            newParents.append(newNode)

        newParents.append(lastChild)
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