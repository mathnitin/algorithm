'''
Convert an integer to roman variable.
'''

#!/bin/python

class IntegerToRoman():
    def __init__(self):
        self.__d = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: 'MMMM'}
    
    def _getRoman(self, num):
        return self.__d[num]

    def convert(self, N):
        if N < 1 or N > 4999:
            return ''

        ans = []
        mult = 1
        while N != 0:
            ans = [self._getRoman((N%10)*mult)] + ans
            mult *= 10
            N /= 10

        return ''.join(ans)

if __name__ == "__main__":
    print IntegerToRoman().convert(3974)
