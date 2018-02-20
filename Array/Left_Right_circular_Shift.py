#!/bin/python

'''
Queries on Left and Right Circular shift on array

Given an array A of N integers. There are three type of type of commands:

1 x : Right Circular Shift the array x times. If an array is a[0], a[1], ..., a[n-1], then after one right circular shift the array will become a[n-1], a[0], a[1], ... a[n-2].
2 y : Left Circular Shift the array y times. If an array is a[0], a[1], ..., a[n-1], the after one left circular shif the array will become a[1], ..., a[n-2], a[n-1], a[0].
3 l r : Print the sum of all integers in the subarray a[l...r] (l and r inclusive).
Given Q queries, the task is execute each query.

Examples:

Input : n = 5, arr[] = { 1, 2, 3, 4, 5 }
        query 1 = { 1, 3 }
        query 2 = { 3, 0, 2 }
        query 3 = { 2, 1 }
        query 4 = { 3, 1, 4 }
Output : 12
         11
Initial array arr[] = { 1, 2, 3, 4, 5 }
After query 1, arr[] = { 3, 4, 5, 1, 2 }.
After query 2, sum from index 0 to index 
               2 is 12, so output 12.
After query 3, arr[] = { 4, 5, 1, 2, 3 }.
After query 4, sum from index 1 to index 
               4 is 11, so output 11.
'''

def query1(arr, rShift):
    temp = arr*2
    return temp[rShift:len(arr)+rShift-1]

def query2(arr, lShift):
    temp = arr*3
    return temp[len(arr)-lShift:(2*len(arr)-1)]

def query3(arr, l, r):
    sum = 0
    print arr
    for i in range(l,l+r):
        sum += arr[i]
    return sum

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    arr = query1(arr, 3)
    print query3(arr, 0, 2)
    arr = query2(arr, 1)
    print query3(arr, 1, 4)