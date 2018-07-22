#!/bin/python
'''
Find if a given number has exactly three factors

Explanation:
2 of the fatcors are 1 and n. A number which is a square will only have 3 factors.
'''

def is_perfect_square(n):
    x = n / 2
    y = set([x])
    while x * x != n:
        x = (x + (n / x)) / 2
        if x in y: return False
        y.add(x)
    return True

if __name__ == "__main__":
    n=9
    print is_perfect_square(n)
