## Return a frequency table of characters given a string
## Asked follow up questions about non-english letters and how I might tackle that with a regex
import re
def freqTable(word):
    #word might not be english letters...
    #pseudocode: replace non-letters in unicode
    word.replace(, "") 
    word = re.filter([a-z])
    freqTable = {}
    for letter in word:
        if letter in freqTable:
            freqTable[letter] += 1
        else:
            freqTable[letter] = 1
    return freqTable
    
string = "abca"
print freqTable(string)

string = ""
print freqTable(string)

string = "   sdfsdf"
print freqTable(string)

string = "  !!$"
print freqTable(string)

[1 * P_1^n(input[i])  P_{0..i-1}input[i] * P_{i+1}^n input[i])


## Given an array of numbers, return an array where each element in the resulting array is the product of all the other elements
## Asked to improve on the naive approach and then improve on the 
[ 2 3 4 ] => 24  O(n)
[ 12 8 6 ] => [24/2 24/3 24/4] O(n)

def product(arr):
    if (len(arr)<2): 
        return []
    product = []
    for i in range(len(arr)): O(n)
        rest = arr[0:i] + arr[i+1:]
        p = 1
        p*=j for j in rest O(n)
        product.append(p)
    return product

def product2(arr):
    if (len(arr)<2): 
        return []
        
    # account for zeros!
    z_index = arr.indexOf(0)
    if (z_index >= 0):
        #at least one zero exists, we find second index
        z_second_index = arr.remove(0).indexOf(0)
        if z_second_index >=0:
            #two zeros, return list of zeros
            return [0,]*len(arr)
        else:
            # exactly one zero in this case, reconstruct the array
            return [0,]*z_index + [prod(arr.remove(0))] + [0,]*(len(arr)-z_index)
            
    product = prod(arr)
    result = []
    for num in arr:
        if num == 0:
            result.append(zero_product)
        else:
            result.append(float(product/num))
    return result
    
[1 * P_1^n(input[i])  P_{0..i-1}input[i] * P_{i+1}^n input[i])
[]
[2]
[2 4]
[0 3 4] #python throws an exception
=> [0 0 0 0]
[3 2 4]