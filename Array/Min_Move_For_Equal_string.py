#!/bin/python

'''
Minimum move to end operations to make all strings equal
2.8
Given n strings that are permutations of each other. We need to make all strings same with an operation that takes front character of any string and move it to end.

Input : n = 2
        arr[] = {"molzv", "lzvmo"}
Output : 2
Explanation: In first string, we remove
first element("m") from first string and 
append it end. Then we move second character
of first string and move it to end. So after
2 operations, both strings become same.

Input : n = 3
        arr[] = {"kc", "kc", "kc"}
Output : 0
Explanation: already all strings are equal.
'''

def countOper(arr, index):
    totalOperations = 0
    findString = arr[index]
    for i in arr:
        j = 0
        tempString = i*2
        while findString != tempString[j:(j+len(arr[index]))]:
            j +=1 
        totalOperations += j
    return totalOperations

if __name__ == "__main__":
    arr = ["xzzwo", "zwoxz", "zzwox", "xzzwo"]
    out = None
    for i in xrange(len(arr)):
        count = countOper(arr, i)
        if out == None:
            out = count
        if count < out:
            out = count
    print out
    