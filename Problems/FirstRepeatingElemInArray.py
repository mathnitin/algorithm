#!/bin/python

'''
https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

Find the first repeating element in an array of integers
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Examples:

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]
'''


if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6]
    dic = {}
    countArr = [1] * len(arr)
    result = None
    for index in range (len(arr)):
        elem = arr[index]
        if elem in dic:
            oldIndex = dic[elem]
            countArr[oldIndex] += 1
        else:
            dic[elem] = index
    for index in range (len(countArr)):
        if countArr[index] > 1:
            result = arr[index]
            break
    if result is None:
        print 'No element is repeated'
    else:
        print result