Evernote - Ammar Khaku

Web teams:
  Services Team = Full stack development, backend design, SQL tables, web services side (4 developers)
  Commerce Team = Payment portals (paypal, alipay, etc...)
  Market Team = Market team (4 developers)
  Platform team = Backend caching infrastruction
  Business team = also part of code base

How many developers per team? (20 developers total)


# Given an array, write a function that outputs an array that the product of all the other elements
arr = [2, 1, 3, 4]
output = [0, 24, 0, 0]
[] => error
[1] => [1]

input =  2     1     3    4
output = 12    24    8    6

         12    12    4    1
         1     2     2    6
range(3)
0, 1, 2

cache_for = {}
cache_back = {}
def preprocess(arr):
    product = 1
    for i in range(len(arr)):
        cache_for[i] = product
        product *= arr[i]
    product = 1
    for i in range(len(arr), reverse=True):
        cache_back[i] = product
        product *= arr[i]
    
def product(arr):
    output = []
    preprocess(arr)
    for i in range(len(arr)):
        output[i] = cache_for[i] * cache_back[i]
    return output

def dealWithZeros(arr):
    #dealing with zeros
    if (z_index >= 0):
        #at least one zero
        arr.remove(z_index)
        z_index_2 = arr.indexOf(0) #O(n)
        if (z_index_2 >= 0):
            #two zeros:
            return [0]*(len(arr)+1)
        else:
            total_product = prod(arr)
            return [0]*z_index+[total_product]+(len(arr)-z_index-1)*[0]

def product(arr):
    if (arr == []):
        raise Exception("no arrays of length 0 allowed!")
    if (len(arr)==1):
        return [1]
    z_index = arr.indexOf(0) #O(n)
    
    if (dealWithZeros(arr)):
        return
    
    output = []
    total_product = prod(arr)
    for i, elem in enumerate(arr): #O(n)
        output[i] = total_product/elem
        
    return output