#!/bin/python

'''
Cound odd numbers between any number m and n
'''

if __name__ == "__main__":
    i = 2
    j = 10
    count = (j-i)/2
    if i%2 != 0 and j%2 != 0:
        count -= 1
    print count