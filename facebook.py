#Hey Dave, I'm Sherman!

#Palindrome

#1) kayak
#2) racecar
#3) Madam I'm Adam #punctuation?
#4) A man, a plan, a canal, Panama!



def isPalindrome (word):
    #replace everything that is not a letter, with ""
    word.replace("![a-z]","").lowercase() #O(n) 
    while (len(word)!=1 and len(word)!=0):
        if (word[0] != word[-1]):
            return False
        word = word[1:-1]
    return True
       
def isPalindromeHelper(word):
    if (len(word) ==1 or len(word)==0)
        return True
    if (word[0] != word[-1]):
        return False
    else:
        return isPalindromeHelper(word[1:-1]) #chops off first and last letter
   


# Problem 2:

# Given a list of words: how might you find the longest palindrome that you have in this word

# dict = ["im", "kayak", "racecar", "madam", "adam"]

# answer = "madam im adam"

   
def isPalindrome (word):
    #replace everything that is not a letter, with ""
    word.replace("![a-z]","").lowercase() #O(n) 
    while (len(word)!=1 and len(word)!=0):
        if (word[0] != word[-1]):
            return False
        word = word[1:-1]
    return True

longestPalindrome = ""
def getPerms(words):
    if (len(words) == 1):
        return words
    else:
        perms = []
        for i in range(0:len(words)): #O(n)
            perms.append(words[:i] + words[0] + words[i:])
        for perm in perms:
            candidate = "".join(perm)
            if isPalindrome(candidate) and len(candidate) > len(longestPalindrome):
                 longestPalindrome = candidate
            getPerms(perm[1:]) #O(n)
        return longestPalindrome

        
   
1 2 3 4 #j = 0, i=1 to 4


   