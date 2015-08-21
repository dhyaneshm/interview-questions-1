
numeralHash = {
    "I": 1,
    "V": 5,
    "X": 10,
    
    "L": 50,
    "C": 100,
    
    "D": 500,
    "M": 1000
}

subtractHash = {
    "I": {"V","X"},
    "X": {"L","C"},
    "C": {"D","M"}
}

"""
Method: shouldSubtract
Input: a current number and the next number in the sequence
Return if the current number's value should be subtracted or not
"""
# num = X, nextNum = I
# subtractHash[num] = {L, C}
def shouldSubtract(num, nextNum):
    if num not in subtractHash: return False
    return nextNum in subtractHash[num]
"""
Method: convertToNumber
Input: an string representing a roman numeral
Given a numeral, return an integer
"""
def convertToNumber(numeral):
    result = 0
    for i, num in enumerate(numeral): #LXI, result = 61
        subtractFlag = False
        if i < (len(numeral)-1):
            subtractFlag = shouldSubtract(num, numeral[i+1])
        value = numeralHash[num]
        if (subtractFlag):
            value *= -1
        result += value
    return result

convertHash = {
    0: ("I", "V", "X"),
    1: ("X", "L" , "C"), # imagine these are all strings
    2: ("C", "D", "M"),
    3: ("M", "v", "x")
}
# convertHelper(5, 0) -> V
# number = 0, power = 1
# ones = X, fives = L, C

def convertHelper(number, power):
    ones, fives, tens = convertHash[power]
    if (number < 4):
        return number*ones
    if (number == 4):
        return ones+fives
    if (number < 9):
        return fives + (number-5)*ones
    if (number == 9):
        return ones+tens
 
"""
Method: convertToNumeral
Input: an integer
Given a integer, return a roman numeral string
"""
def convertToNumeral(number): 
    power = 0
    remainer = None
    result = ""
    while(number > 0):
        remainer = number % 10  
        result = convertHelper(remainer, power) + result 
        power += 1
        number /= 10
    return result

#Testing numbers up to 1000
for i in range(1000):
    numeral = convertToNumeral(i)
    number = convertToNumber(numeral)
    print str(i) + ": "+numeral + ", " +str(number)
