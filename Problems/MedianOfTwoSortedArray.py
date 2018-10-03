#!/bin/python

'''
https://www.geeksforgeeks.org/median-of-two-sorted-arrays/

Median of two sorted arrays of same size
There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after merging the 
above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)).

Input:
   ar1[] = {1, 12, 15, 26, 38}
   ar2[] = {2, 13, 17, 30, 45}

Output:
    16

Explanation:
    After merging 2 arrays
    1, 2, 12, 13, 15, 17, 26, 30, 38, 45

    Middle 2 elements are 15 and 17.
    So average is (15 + 17)/2 = 16
'''

def median(arr):
    size = len(arr)
    if size%2 == 0:
        return (arr[size/2] + arr[size/2 - 1])/2
    else:
        return arr[size/2]


def getMedian(arr1, arr2):
    size = len(arr1)

    if size == 0:
        return -1
    elif size == 1:
        return (arr1[0] + arr2[0])/2
    elif size == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1]))/2

    med1 = median(arr1)
    med2 = median(arr2)
    if med1 == med2:
        return med1
    elif med1 > med2:
        return getMedian(arr1[:size/2+1], arr2[size/2:])
    elif med2 > med1:
        return getMedian(arr1[size/2:], arr2[:size/2+1])
    

if __name__ == "__main__":
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    if len(arr1) != len(arr2):
        print "Doesn't work for arrays of unequal size"
        exit
    print getMedian(arr1, arr2)
