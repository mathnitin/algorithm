#!/bin/python
'''
Program to cyclically rotate an array by one

Given an array, cyclically rotate the array clockwise by one.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}
'''
# Method for rotation
def rotate(arr, n):
    x = arr[n - 1]
#    print "x: ", x
#    print "n: ", n
    for i in range(n - 1, 0, -1):
#        print "i:", i
#        print "arr[i]", arr[i]
#        print "arr[i-1]", arr[i-1]
        arr[i] = arr[i - 1]        
    arr[0] = x
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    arr = rotate(arr, len(arr))
    print arr