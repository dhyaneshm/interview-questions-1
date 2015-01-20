"""
Given an unsorted stack of integers, write a method to sort the integers using only other stacks as a datastructure
========
Example:
input 3 1 2
result = 3 2 1
=============
High-level approach:
Take a 
"""

def sort(input):
    result = Stack.new
    temp = Stack.new
    while (not input.isEmpty()): # O(n)
        cur = input.pop()
        #compare top of the result stack with my current
        while (not result.isEmpty() and cur < result.peek()): # O(n) worst case
            #keep popping the result stack until I find a number that cur is > 
            temp.push(result.pop())
        result.push(cur)
        while (not temp.isEmpty()) # O(n)
            result.push(temp.pop())
    return result
    
"""
Given a Node class with the following methods, write a method that returns the least common ancestor of two nodes in a BST
Class Node:
    def getValue():
        ...
    def getLeft():
        ...
    def getRight():
        ...
==========
Example:
        A
     B    c
  D    E

root = A
child1 = D
child2 = E
============
High Level approach:
1. Compose the paths from the root to the two target children. 
2. Find the first point of divergence in their paths and that will be the LCA

root -> child1 = [A, B, D]
root -> child2 = [A, B, E]
return B
"""
def search(cur, target, path):
    if (cur == NULL):
        return None
    if (cur.getValue() == target):
        return path
    else:
        left = search(cur.getLeft(), target, path.append(cur.getLeft()))
        right = search(cur.getRight(), target, path.append(cur.getRight()))
        if (left == None and right == None):
            return None
        if (left == None):
            return right
        else:
            return left
        

def LCA(root, child1, child2):
    #find root->child1
    firstPath = search(root, child1)
    secondPath = search(root, child2)
    for elem, i in enumerate(firstPath):
        if elem === secondPath[i]
    
    
        
        










    
