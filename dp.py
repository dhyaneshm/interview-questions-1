#some practice for dynamic programming algorithms

# Bottom-up approach for solving minimum actions taken to get to 1:
def bottomUpApproach(n):
  cache = {}
  cache[1] = 0
  for i in range(2, n+1):
    cache[i] = 1 + cache[i-1]
    if (i%2==0):
      cache[i] = min(cache[i], 1 + cache[i/2])
    if (i%3==0):
      cache[i] = min(cache[i], 1 + cache[i/3])
  return cache[n] 

# print bottomUpApproach(25)

# Returns the minimum number of coins needed to exact change
DENOMINATIONS = [1,5,10,25]
def minCoins(change):
  cache = {}
  cache[0] = 0
  cache[1] = 1
  for i in range(2, change+1):
    best = float('inf')
    for amt in DENOMINATIONS:
      if i > amt:
        best = min(best, cache[i-amt] + 1)
    cache[i] = best
  return cache[change]

# print minCoins(0)
