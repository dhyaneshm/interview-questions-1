# First question. Imagine you're a host: getting bunch of requests as integer array. Each integer represents a number of nights as back to back reservations. You can pick as a host which requests to take given a constraint - you need one day in between to book a place. Maximizing the total number of nights stayed where.

# [5, 1, 1, 5] => 10

# [3, 6, 4] => 7
# [3, 9, 4] => 9
# [4, 10, 3, 1, 5] => 15

# Nov 1 - Nov 5
# Nov 5 - 6
# Nov 6 - 7
# Nov 7 - 12

# Two high level approaches: CSP, recursion
# CSP - constraints on no two variables back to back, maximizing the auxillary variable sum
# recursion - pare down the array until you have none left, keeping track of the sum so far, and maximize your recursive calls

def maximizeNights(arr):
    
    cache = {}
    #maximizing nights
    def recurse(arr, nights, index):
        if (index in cache):
            return cache[index]
        if (len(arr) == 0):
            return nights
        if (len(arr) == 1):
            cache[index] = nights + arr[0]
            return cache[index]
        else:
            keepNight = 0            
            if (len(arr) > 2):
                keepNight = recurse(arr[2:], nights+arr[0], index + 2)
            discardNight = recurse(arr[1:], nights, index + 1)
            cache[index] = max(keepNight, discardNight)
            return cache[index]
    return recurse(arr, 0, 0)

print maximizeNights([4, 10, 3, 1, 5])
        