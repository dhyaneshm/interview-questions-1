import collections


def findSubset(str1, str2):
  freq = collections.Counter(str1)
  for char in str2:
    if char not in freq:
      return False
    if freq[char] == 0:
      return false
    else:
      freq[char] -= 1
  return True

def maxInserts(str1, str2):
  sorted1 = sorted(str1)
  sorted2 = sorted(str2)
  indels = 0
  while len(sorted1) > 0:
    if sorted1[0] == sorted2[0]:
      del sorted2[0]
    else:
      indels+=1
    del sorted1[0]
  return indels


print maxInserts("hello", "elo")