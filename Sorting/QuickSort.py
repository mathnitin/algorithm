#!/bin/python
'''
Implement Quick sort

Random quicksort   O(nlog(n))
Regular quicksort  O(n^2)
'''

import random

'''
def quickSortRand(arr, low, high):
    if low < high:
        pi = partitionRand(arr, low, high)
        quickSortRand(arr, low, pi-1)
        quickSortRand(arr, pi+1, low)

def partitionRand(arr, low, high):
    randIndex = random.randint(low, high)
    arr[low], arr[randIndex] = arr[randIndex], arr[low]
    i = low
    j = i+1
    pivot = arr[low]
    for j in range(j, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i
'''

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)    

def partition(arr, low, high):
    i = low
    j = i+1
    pivot = arr[low]

    for j in range(j, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[low] = arr[low], arr[i]
    return i

if __name__ == "__main__":
    arr = [6,10,13,5,8,3,2,11]
    print arr
    quickSort(arr, 0, (len(arr)-1))
    print arr