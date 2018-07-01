#problem2 - Even Fibonacci numbers

#!/bin/python3

import sys

def getsumofevenfibonumbers(n):
    a,b,sumofeven = 1,1,[]
    while a + b < n:
        if (a + b) % 2 == 0 :
            sumofeven.append(a+b)
        b = a + b
        a = b - a
    return sum(sumofeven)    
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = getsumofevenfibonumbers(n)
    print(result)
    
