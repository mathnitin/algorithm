#!/bin/python

'''
Three way partitioning of an array around a given range

Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVVal come next.
3) All elements greater than highVVal appear in the end.
The individual elements of three sets can appear in any order.

Examples:

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
        lowVal = 14, highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
       lowVal = 20, highVal = 20       
Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54} 
'''

def quickSelect(arr, low, high):
    i = low
    j = i+1
    pivot = arr[low]

    for j in range(j, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]

if __name__ == "__main__" :
    arr = [1, 14, 5, 20, 4, 2, 54, 16, 87, 98, 3, 1, 32]
    lowVal = 14
    highVal = 20
    # Find the lowIndex and highIndex
    for index in range(len(arr)):
        if arr[index] == lowVal or arr[index] == highVal:
            print "arr[index]" , arr[index]
            arr[index], arr[0] = arr[0], arr[index]
            print "before arr", arr
            quickSelect(arr, 0, len(arr)-1)
            print "after arr", arr

    print "Ans: ", arr