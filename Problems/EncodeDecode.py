#!/bin/python
'''
Encode and decode a given string. ASCII range supported 32 to 126 (inclusive)

Encode:
    Replace each character with its ASCII value representation. 
    Reverse the string.

Decode:
    Reverse the string.
    Replace ASCII value to character.
'''

def decode(input):
    flipped = input[::-1]
    output = ''
    i = 0
    while i < len(flipped):
        tempStr = ''
        if flipped[i] == '1':
            tempStr = tempStr + flipped[i:i+3]
            output += chr(int(tempStr))
            i = i+3
        else:
            tempStr = tempStr + flipped[i:i+2]
            output += chr(int(tempStr))
            i = i+2
    return output

def encode(input):
    tempStr = ''
    for char in input:
        tempStr = tempStr + str((ord(char)))
    flipped = tempStr[::-1]
    return flipped

if __name__=="__main__":
    input = 'GO VMWare'
    print 'Input: ', input
    enc = encode(input)
    print 'Encoded: ', enc
    print 'Decoded: ', decode(enc)