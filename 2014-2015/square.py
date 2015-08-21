# Paul from Payments team (card-processing team)

# Make a crossword solver that takes a dictionary of words and returns a list of candidates that matches a word with letters and blanks

def get_words():
    return map(lambda k: k.upper(), ["aarhus",
        "aaron",
        "ababa",
        "aback",
        "abaft",
        "abandon",
        "abandoned",
        "abandoning",
        "abandonment",
        "abandons",
        "abase",
        "abased",
        "abasement",
        "abasements",
        "abases",
        "abash",
        "abashed",
        "abashes",
        "abashing",
        "abasing",
        "abate",
        "abated",
        "abatement",
        "abatements",
        "abater",
        "abates",
        "abating",
        "abba",
        "babbled",
        "babbles",
        "babbling",
        "babcock",
        "babe",
        "babel",
        "babelize",
        "babelizes",
        "babes",
        "babied",
        "babies",
        "babka",
        "baboon",
        "fluffiest",
        "gashes",
        "grounder",
        "hickman",
        "impersonate",
        "instrumentally",
        "journalize",
        "legacy",
        "madness",
        "merle",
        "mottoes",
        "notarize",
        "overhears",
        "perfectness",
        "polluted",
        "promoter"])



class Node:
    def __init__(self, value):
        self.value = value
        self.next = {}
    
    def add_node(self, next_char, next_node):
        self.next[next_char] = next_node
        
    def is_next(self, next_char):
        return next_char in  self.next 
    
    def get_next(self, next_letter):
        if next_letter in self.next:
            return self.next[next_letter]
        else:
            return None

def make_trie(words):
    root = Node("ROOT")
    for word in words:
        cur = root
        for letter in word:
            if not cur.is_next(letter):
                newNode = Node(letter)
                cur.add_node(letter, newNode)
            cur = cur.next[letter]
    return root
            
                
class CrosswordSolver:
    def __init__(self):
        '''
      Responsible for returning a list of matching words.
      This class is initialized with a list of words and should be pre-processed as necessary, to facilitate fast lookup.
      "Solve" should return a subset of words from the given dictionary that match the given "target".

      Examples:
      solver.solve("B*D") => ["BAD", "BED"]
      solver.solve("B***") => ["BUMP", "BROW", "BRAT", "BOTH", ...]
      solver.solve("**A**") => ["YEARN", "SWAMP", "CRASH", ...
      '''
        word_families = {}
        words = get_words()
        for word in words:
            if len(word) in word_families:
                word_families[len(word)].append(word)
            else:
                word_families[len(word)] = [word]

        tries = {}
    #     print word_families
        for length in word_families:
            tries[length] = make_trie(word_families[length])
        self.tries = tries

    def solve(self,target):
        if len(target) not in self.tries:
            return []
        cur = self.tries[len(target)]
        if cur == None:
            return []
        candidates = []
        
        def recurse(cur, word, candidate):
            if (len(word)==0):
                candidates.append(candidate)
                return
            if cur == None:
                return
            if (word[0] == "*"):
                # recurse down all possible next paths
                for nextLetter in cur.next:
                    recurse(cur.next[nextLetter], word[1:], candidate+nextLetter)
            else:
                nextNode = cur.get_next(word[0])
                recurse(nextNode, word[1:], candidate+word[0])
        recurse(cur, target, "")
        return candidates


if __name__ == "__main__":
    solver = CrosswordSolver()
    print solver.solve("B*D")
    print solver.solve("ABAS*")
    print solver.solve("**************")
