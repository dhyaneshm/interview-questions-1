# Interviewed with Elijah Meerson who comes from a big company backgroudn looking for ways to get involved in healthcare
# There's a mix of industry and academic people working on the Data science front at Flatiron
# Flatiron is >100 people now and growing fast

# [11001, 11005, 11002, 11003, 20430.... ]
# [11005, 11001 - 11003, 20430]
# High level goal: take an array of zipcodes and return a
# condensed array with any consecutive numbers collapsed into a range

# [11001, 11002] => [11001 - 11002]

def collapseArray(arr):
    if (len(arr) <= 1): return arr
    arr = sorted(arr)
    prev = arr[0]
    collapsedArr = []
    startRange = None
    cur = None
    consecutiveFlag =  False
    for val in arr[1:]: # [11001, 11002]
        cur = val
        if !consecutiveFlag and ((cur - prev) == 1):
            # we have a consecutive zip code here 
            # (and starting a new range with prev as the start of the range)
            consecutiveFlag = True
            startRange = prev
        elif (consecutiveFlag and ((cur - prev) != 1):
            # we end the array range (prev is the last element in the range)
            collapsedArr.append(str(startRange)+'-'+str(prev))
            consecutiveFlag = False
        elif (!consecutiveFlag):
            # we are not inside a consecutive range, so we are free to append the prev number
            collapsedArr.append(prev)
        prev = cur
    if consecutiveFlag and ((cur - prev) == 1):
        collapsedArr.append(str(startRange)+'-'+str(cur))
    else:
        collapsedArr.append(cur)
    return collapsedArr