Q: Write a function to remove the duplicated characters from a string, 
and maintain the order of the characters.

ex. “abracadabra” → “abrcd”
ex. " b  " -> " b" (keep the first space)

2 approaches:
traversal approach
"abrac" 
a -> "brac"
O(n^2)

hash approach

#if word = "abcb"
def removeDups(word):
    hash = {}
    for letter in word: #this loops by value, not by index
        if (letter in hash):
            hash[letter] = True
        else: #only for duplicates, remove!   
            word.remove(letter)
    return word
            
TEST:
    hash = {a: True, b: True, c:True}
    newWord = "abc"
ANALYSIS:
    Runtime: O(n)
    Space: O(n)
    


Question 1: How to delete the current node in a linked list, without knowledge of parent in O(1)?

# edge case, if next node is NULL:
# par -> cur -> NULL
# par -> NULL
if (current->next == NULL):
    current = NULL
    return

#update value of current node
current.value = current->next.value

#update current's pointer
current->next = current->next->next

Question 2: Write a function to iteratively calculate the nth element in the Fibonacci sequence.
Let’s say the 0th is 1.

Fibonacci: 1,1,2,3,5,8,13, ...

n=3, get back 3
int fibonacci(int n) {
    if (n<0) {
        println("ERROR: no negative numbers in fibonacci!");
        return -1;
    }
    int prev = 1;
    int cur = 1;
    int next = cur;
    while (n > 1) {
        next = prev+cur;
        prev = cur;
        cur = next;
        n -= 1;
    }
    return next;
}