#! /bin/python

'''
Reversal algorithm for right rotation of an array

Given an array, right rotate it by k elements.

After K=3 rotation


Examples:

    Input: arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    k = 3
    Output: 8 9 10 1 2 3 4 5 6 7

    Input: arr[] = {121, 232, 33, 43 ,5}
    k = 2
    Output: 43 5 121 232 33
'''

def reverseArray(arr, start, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 3
    # First reverse the entire array
    reverseArray(arr,0, (len(arr)-1))
    # Reverse the first part of the arr, meaning 0 to key-1 index
    reverseArray(arr, 0, key-1)
    # Reverse the second part of the arr, meaning key to len(arr)-1
    reverseArray(arr, key, (len(arr)-1))
    print arr