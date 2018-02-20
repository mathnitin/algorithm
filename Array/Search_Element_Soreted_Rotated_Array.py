#!/bin/python

'''
Search an element in a sorted and rotated array

An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.

{3, 4, 5, 1, 2}

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}
        key = 10   
Output : Found at index 3
'''
def findPivot(arr, start, end):
    if end == 2:
        if arr[0] > arr[1]:
            return 1
        else :
            return 0
    mid = (start + end)/ 2
    while not (arr[mid -1] > arr[mid] < arr[mid+1]):
        if arr[mid] > arr[start]:
            start = mid
        elif arr [mid] < arr[end-1]:
            end = mid
        mid = (start + end)/2
    return mid

def binarySearch(arr, start, end, key):
    mid = (start+end)/2
    if start > end:
        return "Not found"
    if arr[mid] == key:
        return mid
#    print 'start: ', arr[start]
#    print 'arr[start]: ', arr[start]
#    print 'end: ', end
#    print 'arr[end]: ', arr[end]
#    print 'mid: ', mid
#    print 'arr[mid]: ', arr[mid]
    if key > arr[mid]:
        return binarySearch(arr, mid+1, end, key)
    else:
        return binarySearch(arr,start, mid-1, key)

if __name__ == "__main__":
    arr = [30, 40, 50, 10, 20]
    key = 10
    size = len(arr)
    pivotIndex = findPivot(arr, 0, size)
    if (arr[0] <= key <= arr[pivotIndex-1]):
        print binarySearch(arr, 0, (pivotIndex-1), key)
    else:
        print binarySearch(arr, (pivotIndex), (size-1), key)  