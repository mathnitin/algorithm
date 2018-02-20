#!/nim/python

'''
Given a sorted and rotated array, find if there is a pair with a given sum
Given an array that is sorted and then rotated around an unknown point. Find if array has a pair with given sum 'x'. It may be assumed that all elements in array are distinct.

Examples:

Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
Output: true
There is a pair (6, 10) with sum 16

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
Output: true
There is a pair (26, 9) with sum 35

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
Output: false
There is no pair with sum 45.
'''

def pairInSortedRotated( arr, n, x ):
    # Find the pivot element
    for i in range(0, n - 1):
        if (arr[i] > arr[i + 1]):
            break
             
    # l is now index of minimum element        
    l = (i + 1) % n
    # r is now index of maximum element
    r = i     
 
    # Keep moving either l or r till they meet
    while (l != r):
        # If we find a pair with sum x, we return True
        if (arr[l] + arr[r] == x):
            return True
        # If current pair sum is less, move to the higher sum
        if (arr[l] + arr[r] < x):
            l = (l + 1) % n
        else:
            # Move to the lower sum side
            r = (n + r - 1) % n
    return False

if __name__ == "__main__": 
    # Driver program to test above function 
    arr = [11, 15, 26, 38, 9, 10]
    sum = 19
    n = len(arr)
 
    if (pairInSortedRotated(arr, n, sum)):
        print "Array has two elements with sum", sum
    else:
        print "Array doesn't have two elements with sum", sum
