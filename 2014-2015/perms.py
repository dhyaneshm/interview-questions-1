import itertools

def all_perms(elements):
  return itertools.permutations(elements)

for perm in all_perms("abcd"):
  for p in all_perms(perm[1:]):
    print p