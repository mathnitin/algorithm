#!/bin/python

'''
Compute Finonaci series in O(n)
'''

def fibonaci(n):
    data = {}
    data[0] = 0
    data[1] = 1
    for i in range(2,n+1):
        data[i] = data[i-2] + data[i-1]
    return data[n]

if __name__ == "__main__":
    for i in range (0,10):
        print i, ":", fibonaci(i)