#!/bin/python
'''
Determine if a number is an Armsrtong Number.

For example:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1253
Output : No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
'''

import math

def armstrongNumber(num):
    tempNum = num
    numbArray = []
    while tempNum != 0:
        numbArray.append(tempNum%10)
        tempNum = tempNum / 10
    size = len(numbArray)
    total = 0
    for numb in numbArray:
        total = total + math.pow(numb,size)
        if total > num:
            break
    if total == num:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    num = 153
    print armstrongNumber(num)
    num = 120
    print armstrongNumber(num)
    num = 1253
    print armstrongNumber(num)
    num = 1634
    print armstrongNumber(num)