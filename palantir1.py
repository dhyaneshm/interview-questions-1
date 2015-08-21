# find unique intersecting set from two lists of integers
def findIntersectingSet(list1, list2):
    alreadySeen = set(list1)
    intersection = set()
    for num in list2:
        if num in alreadySeen:
            intersection.add(num)
    return intersection

# Test case
findIntersectingList([1,2,3], [1,4,1]) # -> [1]

## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.



'''

Given an immutable mxn 2d array of integers, where: 

   0 represents water

> 0 represents a piece of land with a value, 

find the most valuable island and return its value. An island is defined as any contiguous 

grouping of land, connected by NSEW, not diagonally.

[0,0,0,1,0]

[0,2,1,1,0]

[0,0,0,0,4]

[3,5,0,0,0]

'''
def checkBounds(matrix, i, j):
    return i > -1 and i < len(matrix) and j > -1 and j < len(matrix[0])

def findValueOfIsland(matrix, i, j, alreadySeen):
    if (matrix[i][j] == 0 or not checkBounds(matrix, i, j) or (i,j) in alreadySeen):
        return 0
    alreadySeen.add((i,j))
    return matrix[i][j] + findValueOfIsland(matrix, i-1, j, alreadySeen) 
     + findValueOfIsland(matrix, i, j-1, alreadySeen)
     + findValueOfIsland(matrix, i, j+1, alreadySeen)
     + findValueOfIsland(matrix, i+1, j, alreadySeen)
    

def findLargestIsland(matrix):
    alreadySeen = set()
    maxValue = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(matrix):
            if val > 0 and (i,j) not in alreadySeen:
                # start searching
                value = findValueOfIsland(matrix, i, j, alreadySeen)
                if (value > maxValue):
                    maxValue = value
    return maxValue
                


