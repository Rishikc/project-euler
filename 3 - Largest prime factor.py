#problem3 - Largest prime factor

#!/bin/python3

import sys

def largestPimeFactor(n):
    i = 2
    while i * i <= n:
        while n % i == 0 :
            n //= i
        i = i + 1
    if n > 1 :
        return n
    return i-1  

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = largestPimeFactor(n)
    print(result)
