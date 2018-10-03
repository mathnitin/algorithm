#!/bin/pyhton

'''
https://www.geeksforgeeks.org/python-count-prefixes-given-string-greatest-frequency/

Python | Count all prefixes in given string with greatest frequency
Given a string, print and count all prefixes in which first alphabet has greater frequency than second alphabet.

Take two alphabets from the user and compare them. The prefixes in which the alphabet given first has greater frequency than the second alphabet, such prefixes are printed, else the result will be 0.

Examples :

Input : string1 = "geek", 
        alphabet1 = "e", alphabet2 = "k"
Output :
ge
gee
geek
3

Input : string1 = "geek",
        alphabet1 = "k", alphabet2 = "e"
Output :
0
'''

def prefix(string, alphabet1, alphabet2):
    outStr = ""
    count = 0 
    alphabet1Freq = 0
    alphabet2Freq = 0
    for index in range(len(string)):
        outStr += string[index]
        if string[index] == alphabet1:
            alphabet1Freq += 1
        elif string[index] == alphabet2:
            alphabet2Freq += 1
        
        if alphabet1Freq > alphabet2Freq:
            print outStr
            count += 1
    return count


if __name__ == "__main__":
    string = "geeksforgeeks"
    alphabet1 = "e"
    alphabet2 = "g"
    print prefix(string, alphabet1, alphabet2)