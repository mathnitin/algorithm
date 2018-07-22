#!/bin/python

'''
Implement counting sort.
O(n+k) --> where k is the range.
'''

from collections import OrderedDict

def countingSort(arr, lower, upper):
    count = OrderedDict()
    for i in range (lower, upper+1):
        count[i] = 0
    output = [0 for i in range(len(arr))]
    for val in arr:
        count[val] += 1
    curTotal = 0
    for key, val in count.items():
        curTotal += val
        count[key] = curTotal
    for val in arr:
        index = count[val]
        count[val] = count[val]-1
        output[index-1] = val
    return output


if __name__ == "__main__":
    arr = [3, 4, 3, 2, 7, 5, 2]
    print arr
    print countingSort(arr, 0,9)
