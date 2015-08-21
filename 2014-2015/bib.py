import time
def getNextPositions(cur):
  nextPositions = []
  for delta in [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,-2),(-1,2)]:
    next = (delta[0]+cur[0], delta[1]+cur[1])
    if (next[0]>=0 and next[1]>=0 and next[0]<=2 and next[1]<=2 or (next[0]==3 and next[1]==1) ):
      nextPositions.append(next)
  return nextPositions

cache = {}
def calling(numDigits):
  def recurse(pos, numDigits):
    if numDigits == 0: return 0
    if numDigits == 1: return 1
    if (pos[0],pos[1],numDigits) in cache:
      return cache[(pos[0],pos[1],numDigits)]
    else:
      answer = 0
      for nextPos in getNextPositions(pos):
        answer+=recurse(nextPos, numDigits-1)
      cache[(pos[0],pos[1],numDigits)] = answer
      return answer
  return recurse((0,0), numDigits)
start = time.time()
print calling(100)
print str(time.time() - start) + " sec elapsed"