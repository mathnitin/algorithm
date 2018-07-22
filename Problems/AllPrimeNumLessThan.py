#!/bin/python
'''
Generate all prime numbers less than a given number.
'''

if __name__ == "__main__":
    inputNum = 30
    for num in range(3, inputNum, 2):
        isPrime = True
        for checkNum in range(2, num, 1):
            if num%checkNum == 0:
                isPrime = False
                break
        if isPrime == True:
            print num
