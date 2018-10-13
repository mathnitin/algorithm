#!/bin/python

'''
Pangram Checking
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

Examples: "The quick brown fox jumps over the lazy dog" is a Pangram [Contains all the characters from 'a' to 'z']
"The quick brown fox jumps over the dog" is not a Pangram [Doesn't contains all the characters from 'a' to 'z', as 'l', 'z', 'y' are 
missing]
'''

def checkPanagram(str):
    charList = []
    for i in range(26):
        charList.append(False)
    for char in str.lower():
        if char != ' ':
            charList[(ord(char) - ord('a'))] = True
    if False in charList:
        return False
    return True

if __name__ == "__main__":
    input = "The quick brown fox jumps over the lazy dog"
    print checkPanagram(input)
    input="The quick brown fox jumps over the dog"
    print checkPanagram(input)