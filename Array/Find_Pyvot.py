#!/bin/python

'''
Find the minimum element in a sorted and rotated array

A sorted array is rotated at some unknown point, find the minimum element in it.

Following solution assumes that all elements are distinct.

Examples

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1
'''
def findPyvot(arr):
    for i in xrange(1, (len(arr)-1), 1):
        if arr[i-1] > arr[i] < arr[i+1]:
            return i

if __name__ == "__main__":
    arr = [ 5, 6, 1, 2, 3, 4]
    print findPyvot(arr)