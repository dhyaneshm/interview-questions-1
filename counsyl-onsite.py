'''
Charlie - billing team from Counsyl
Insurance claims
Looking at insurance data from companies - estimate how much company will reimburse for this test/disease
Target a subset of diseases that have reimbursed well (when you decide what to bill the company)
Filing claims is very complicated

Wet lab team, automation team - quality control, generating the report on patient dna
UI/UX, patient-facing portal 
Tour of Duty
'''

"""
Recursive algorithm to permute a string and return a list of permutations.
"""


def perm(word):
    if (len(word) == 1):
        return [word]
    permutations = []
    rest = perm(word[1:])
    for permutation in rest:
        for i in range(len(permutation)+1):
            newWord = permutation[0:i] + word[0] + permutation[i:]
            permutations.append(newWord)
    return permutations

print perm('abc')

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
        self.value = value
        self.left = None
        self.right = None

def buildTree(triangle):
  #need to build the root!
    rows = triangle.strip().split('\n')
    root = 
    parents = [root]
    
    for row in rows:
        rowVals = row.strip().split(' ')
        newParents = []
        for i in range(len(rowVals)):
            if (i%2 == 1):
                continue
            parent = parents.pop(0)
            leftChild = Node(rowVals[i]) #left child
            rightChild = Node(rowVals[i+1]) 
            parent.left = leftChild
            parent.right = rightChild
            newParents.append(leftChild)
            newParents.append(rightChild)
        parents = newParents
    return root
          
root = buildTree(triangle)
    
    

# Dan from Counsyl


'''
Suppose we say that two strings *cipher-match* if their character sequences follow the same sequential pattern, e.g. `abca` and `xyzx` cipher-match because there exists a substitution cipher from one to the other (or, to be more precise, a bijective mapping between character sets): `{'a': 'x', 'b': 'y', 'c': 'z'}`.

# We are given a long list of strings as input to our function, and we wish to write a function to determine the *number of cipher-matching pairs* of input strings.
'''

'''
0120 0120
>>> get_num_cipher_matches(['abca', 'qweq', 'xyzx', 'jklj', 'foobar'])
6
'''

# determine if cipher-match
# verify same length

def cipherMatch(word1, word2):
    if (len(word1) != len(word2)):
        return False
    mapping = {}
    for i, val in enumerate(word1):
        if val in mapping:
            if (word2[i] != mapping[val]):
                return False
        else:
            mapping[val] = word2[i]
    return True


def encode(word):
    map = {}
    counter = 0
    encoded = ""
    for letter in word:
        if letter not in map:
            map[letter] = counter            
            counter += 1
        encoded += str(map[letter])
    return encoded


def get_num_cipher_matches(arr):
    encoded_arr = [encode(word) for word in arr]
    print encoded_arr
    seen = set()
    total = 0
    for word in encoded_arr:
        if word in seen:
            total += 1
        else:
            seen.add(word)
    
    return total

print get_num_cipher_matches(['abca', 'qweq', 'xyzx', 'jklj', 'foobar'])
            
# Last interview was with Bill I think            
# Given k really large files with n total words
# Write all n total words to this output file in sorted order
            
            
# Complimentary string sequence in O(n) time without overhead

'''
Take a genetic sequence, A<->T and C<->G
'''

sequence = 'acgtcgtgcatct'

sequence.replace('a', 'T')
sequence.replace('t', 'A')
sequence.replace('c', 'G')
sequence.replace('g', 'C')
sequence.lowercase()
    
    
    
    
    
    
    
    
    
    
