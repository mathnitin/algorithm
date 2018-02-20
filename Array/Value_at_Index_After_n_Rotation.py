#!/bin/python

'''
Find element at given index after a number of rotations

An array consisting of N integers is given. There are several Right Circular Rotations of range[L..R] that we perform. After performing these rotations, we need to find element at a given index.

Examples:

Input : arr[] : {1, 2, 3, 4, 5}
        ranges[] = { {0, 2}, {0, 3} }
        index : 1
Output : 3
Explanation : After first given rotation {0, 2}
                arr[] = {3, 1, 2, 4, 5}
              After second rotation {0, 3} 
                arr[] = {4, 3, 1, 2, 5}
After all rotations we have element 3 at given
index 1. 
'''

def rightRotation(arr, rotationArr):
    temp = arr*2
    stIndex = rotationArr[0]
    rShift = rotationArr[1]
    return temp[rShift+stIndex:len(arr)+rShift-1+stIndex]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rotations = [[0,2], [0,3]]
    index = 1
    for i in rotations:
        arr = rightRotation(arr,i)
    print arr[index]

