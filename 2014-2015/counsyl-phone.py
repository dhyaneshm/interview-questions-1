# Implement a Lexicon class with the following methods:
#
# add_word: given a word, adds it to the Lexicon
# is_word: boolean function that returns whether the input word is in
#          the Lexicon
# is_prefix: boolean function
class Node:
    self.children = []
    self.value
    self.isEnd = False


root = {value="START" children= [{"d", }]}
letter = "o"
cur_n = {value="d" children=[{o, []}]}

def inChildren(letter, node):
    child_values = [n.value for n in node.children]
    return child_values.indexOf(letter)

class Lexicon:
    def __init__():
        self.root = Node()
        self.root.value = "START"
        
    def add_word(word):
        cur_n = self.root
        for letter in word:
            child_index = inChildren(letter, cur_n)
            if child_index >= 0:
                cur_n = cur_n.children[child_index]
                continue
            new_n = Node()
            new_n.value = letter
            cur_n.children.append(new_n)
            cur_n = new_n
            
    def is_word(word):
        return word in lexicon

    
    