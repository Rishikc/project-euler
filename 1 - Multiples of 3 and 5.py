#problem1 - Multiples of 3 and 5

#!/bin/python3

import sys

def sumofmultiples(i,n):
    n //= i;
    return i * n * (n+1) //2; #

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    a = 3;
    b = 5;
    result = sumofmultiples(a,n-1) + sumofmultiples(b,n-1) - sumofmultiples(a*b,n-1)
    print(result)
