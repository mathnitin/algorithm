#!/bin/python

'''
https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

Python program to check if a string is palindrome or not
Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if reverse of 
the string is same as string. For example, "radar" is palindrome, but "radix" is not palindrome.

Examples:

Input : malayalam
Output : Yes

Input : geeks
Output : No
'''

def palindrome(string):
    stIndex = 0
    endIndex = len(string)-1
    while stIndex < endIndex:
        if string[stIndex] != string[endIndex]:
            return False
        stIndex += 1
        endIndex -= 1
    return True

if __name__ == "__main__":
    string = "malayalam"
    print palindrome(string)