#!/bin/python

'''

Input:   arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
Output:  Index of element is 4
All elements on left of arr[4] are smaller than it
and all elements on right are greater.
 
Input:   arr[] = {5, 1, 4, 4};
Output:  Index of element is -1

'''


if __name__ == "__main__":
    #arr = [5, 1, 4, 3, 6, 3, 8, 10, 8, 9]
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    result, highest = None, 0
    for index in range(len(arr)):
        if result == None:
            if arr[index] > arr[highest]:
                result = index
                highest = index
        else:
            if arr[index] < arr [result]:
                result = None
            else:
                highest = index
    print result