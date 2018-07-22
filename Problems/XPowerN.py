#!/bin/python
'''
Find x power n 
'''
import math

def method1(x, n):
    if x == 0:
        return 0
    ans = 1
    for i in xrange(n):
        ans = x*ans
    return ans

def method2(x, n):
    even = False
    retval = 0
    if n%2 == 0:
        retval = 2*math.pow(x,(n/2))
    elif even == False:
        retval = 2*math.pow(x,(n/2))*x
    return retval

if __name__ == "__main__":
    n = 3
    x = 2
    print method1(x,n)
    print int(method2(x,n))
