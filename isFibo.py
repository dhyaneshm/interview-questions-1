# Enter your code here. Read input from STDIN. Print output to STDOUT
cache = set()
last = 1
prev = 1
cache.add(1)
def isFibo(num):
    global last
    global prev
    if num in cache:
        return True
    next = last + prev
    cache.add(next)

    while next <= num:
        prev = last
        last = next
        next = prev + last
        cache.add(next)
    if num in cache:
        return True
    return False

T = int(raw_input())
for _ in range(T):
    if isFibo(int(raw_input())):
        print "IsFibo"
    else:
        print "IsNotFibo"
    
    