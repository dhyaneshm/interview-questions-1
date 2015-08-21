# Find all pairs in an array that add up to a particular sum
#[1,3,4,6,7]
# sum = 10
# o/p: [3,7],[4,6]

# O(n) time and space

def findPairs(arr1, total):
    pairMap = {}
    
    for val in arr1:
        if (val not in pairMap and (total-val) not in pairMap):
            pairMap[(total-val)] = (val, total-val)
    
    for val in arr1:
        if val in pairMap:
            print pairMap[val]
            
def findIntersection(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    loopArr = arr2
    if (len(arr1) > len(arr2):
        loopArr = arr1
    #while list is not empty
    while (len(loopArr) != 0):
        if (arr1[0] == arr2[0]):
            print arr1[i], " "
            arr1.pop(0)
            arr2.pop(0)
        elif (arr1[0] < arr2[0]):
            arr1.pop(0)
        else:
            arr2.pop(0)
            
    
    ## attempt 1:
    if (len(arr1) > len(arr2):
        loopLength = len(arr1)
    for i in range(loopLength):
        if (arr1[i] == arr2[i]):
            print arr1[i], " "
        elif (arr1[i] < arr2[i]):
            arr1.removeAt(i)
        else:
            arr2.removeAt(i)
    