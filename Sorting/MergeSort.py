#!/bin/python
'''
Implement merge sort.
'''

def merge(arr, l, mid, r):
    arr1 = arr[l:mid+1]
    arr2 = arr[mid+1:r+1]
    n1 = len(arr1)
    n2 = len(arr2) 
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


def mergeSort(arr, s, e):
    if s < e:
        m = (s + e)/2
        mergeSort(arr, s, m)
        mergeSort(arr, m+1, e)
        merge(arr, s, m, e)

if __name__ == "__main__":
    array = [3,2,5,6,4]
    print array
    mergeSort(array, 0, len(array))    
    print array