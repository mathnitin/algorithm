#!/bin/python

'''
Perform Insertion sort.
'''

def insertionSort(array):
    if len(array) ==1:
        return array
    else:
        j = 1
        while j <len(array):
            i = j
            while i > 0:
                if array[i-1] > array[i]:
                    array[i], array[i-1] = array[i-1], array[i]
                    i = i-1
                else:
                    break
            j = j+1
    return array

if __name__ == "__main__":
    array = [3,2,5,6,4]
    print insertionSort(array)