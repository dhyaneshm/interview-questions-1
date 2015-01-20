# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(raw_input())
count = 0
prevFactorial = 1
for i in range(1,n+1):
    if (prevFactorial % i == (i-1)):
        count+=1
    prevFactorial*=i
print count

(x-1)! % x = (x-1)
find all numbers from 1 to N inclusive that satisfy the above equality