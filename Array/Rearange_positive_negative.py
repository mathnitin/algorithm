#!/bin/python

'''
Rearrange positive and negative numbers with constant extra space

Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional data structure like hash table, arrays, etc. The order of appearance should be maintained.

Examples:

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
'''

if __name__ == "__main__":
    p = -1
    pSet = False
    n = -1
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    for i in xrange(len(arr)):
        if arr[i] >= 0:
            if pSet == False:
                p = i
                pSet = True
        if arr[i] < 0:
            temp = arr[i]
            cur_index = i
            while cur_index != p:
                arr[cur_index] = arr[cur_index-1]
                cur_index = cur_index-1
            arr[cur_index] = temp
            pSet = False
            while cur_index != i and pSet == False:
                if arr[cur_index] >= 0:
                    p = cur_index
                    pSet = True
                cur_index += 1
    print arr

