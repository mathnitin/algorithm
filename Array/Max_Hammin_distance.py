#!/bin/python

'''
Find a rotation with maximum hamming distance
2.2
Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum.
Hamming distance between two arrays or strings of equal length is the number of positions at which the corresponding character(elements) are different.

Note: There can be more than one output for the given input.

Examples:

Input :  1 4 1
Output :  2
Explanation:  
Maximum hamming distance = 2.
We get this hamming distance with 4 1 1 
or 1 1 4 

input :  N = 4
         2 4 8 0
output :  4
Explanation: 
Maximum hamming distance = 4
We get this hamming distance with 4 8 0 2.
All the places can be occupied by another digit.
Other solutions can be 8 0 2 4, 4 0 2 8 etc.  
'''

if __name__ == "__main__":
    arr = [1, 4, 1]
    doubArr = arr*2
    out = 0
    stIndex = 0
    while len(arr)+stIndex <= len(doubArr):
        testArr = doubArr[stIndex:(stIndex+len(arr))]
        count = 0
        for i in xrange(len(arr)):
#            print arr[i], testArr[i]
            if arr[i] != testArr[i]:
                count += 1
#        print count
        if count > out:
            out = count
        stIndex += 1
    print out