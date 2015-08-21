"""
Let's play a game of Boggle! Given a grid with characters (e.g. the following),

EECA
ALEP
HNBO
QTTY

Find all the words that can be formed using the letters in the grid. For instance, you can perform the words elan, celeb, cape, peace, etc.... 
The grid of letters can be used in every direction (see PEACE)
No position can be used twice within the same word. (e.g. POPE is not a valid word on this board)
"""

# Recursive backtracking
# Paramaters: current location, current state of word, the locations that have been visited
# Base cases: if the word is in the dictionary, add it to the list of valid words in the boggle game
# Possible optimizations: isPrefix in the dictionary (requires a Trie structure)

def nextPositions(curPos):
    candidates = []
    candidates.append((curPos[0]+1,curPos[1]))
    candidates.append((curPos[0],curPos[1]))
    ...
    
def findWords(matrix, dictionary):
    def recurse(curPos, curWord, visited, matrix, dictionary, results):
        if not inBounds(curPos, matrix): return
        # requires trie structure
        if not dictionary.isPrefix(curWord) return
        if curWord in dictionary: 
            # note that we should continue to recurse even if we found a word
            results.append(curWord)
            
       # recursively call all positions in the matrix that are one away and have yet to be visited
        visited.add(curPos)
        for nextPos in nextPositions(curPos):
          if nextPos not in visited:
            recurse(nextPos, curWord + matrix[nextPos[0]][nextPos[1]], visited, matrix, dictionary, results)
           
    results = []
    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            visited = set()
            recurse((i,j), letter, visited, matrix, dictionary, results):
    # Note that matrix, results, dictionary is passed by reference in Python but I'll have to deep copy visisted as a list
    
"""
# Parsing number into smaller numbers    
5 = 4 + 1
  = 3 + 2
  = 3 + 1 + 1
  = ...
  = 1 + 1 + .. + 1
3 = 2 + 1 or 1 + 1 + 1
"""
  
def parseNumber(num):
    # returns a list of results given a number = 3
    def recurse(num): # num = 3
        if num == 0: return [[]]
        if num == 1: return [[1]]
        firstNum = num # 2
        secondNum = 0 # 1
        results = []
        # decrement to get first number, and add to the second
        while (firstNum > secondNum):
            for first in recurse(firstNum): #firstNum = 1
                for second in recurse(secondNum): # secondNum = 1
                    # adding the two lists together and then appending their union into the results
                    results.append(first+second) # recurse(2) => [1] + [1], results = [[1,1]]
            firstNum -= 1
            secondNum += 1
        return results
   recurse recurse(num)
    
    
    
    
    