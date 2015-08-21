# Charlie Taveras - Supposed to interview me last time
# Providers team:
#   injecting patient data into their database - lots of unstructured data to sift through
#   any time with specific question: have the nurse practioners go through and train on some patient data before testing on the actual stuff

# CMU 2006: Finance for 6 years
# Time series math, low level C++ 

# Spotify: new york 
# Flatiron: building infrastructure, also building application
# Why interesting problems (intellectually) at Flatiron - can't just give them data




# Given a matrix of pixels, there are continguous pixels that form shapes, the function takes a matrix and returns the number of pixels in the largest shape.

# matrix might not necessarily be square: represent matrix as rows that are not necessarily same length

'''
Returns number of pixels in the largest 'continguous' shape
# high level #1:
# define a recursion that goes to every neighboring pixel and adds one appropriately. the base case would require a tracker for the current number of pixels which it returs
# start the recursion only on a pixel that is actually on...(don't worry about duplicates, cause they should be same number?)
# possibly cache the state at every position so you can just add it without recalculating
'''
def getLargestShape(matrix):
    visited = set()
    
    def recurse(matrix, i, j):
        if (i,j) in visited: 
            return 0
        if i<0 or i>=len(matrix) or j >= len(matrix[i]) or j<0:
            # out of bounds
            return 0
        # only if you're going to add to the shape
        # micro here: only add if the pixel
        visited.add((i, j))
        if matrix[i][j] == 1:
            down = recurse(matrix, i+1, j)
            top = recurse(matrix, i-1, j)
            left = recurse(matrix, i, j-1)
            right = recurse(matrix, i, j+1)
            return down + top + left + right + 1
        # if the current pixel is off
        return 0
            
        
    best = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # microoptimization here
            if matrix[i][j] == 1:
                best = max(recurse(matrix, i, j), best)
    return best

test = [
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 1],
[1, 0, 0, 1, 1]]
print getLargestShape(test)
