#!/bin/python

'''
Implement Binary Search 
'''

class BinarySearch:
    def __init__(self, items):
        self.items = items

    def binarySearch(self, value):
        first = 0
        last = len(self.items) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last)/2
            if value == self.items[midpoint]:
                found = True
            else:
                if value < self.items[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found


if __name__ == "__main__":
    bs = BinarySearch([1,2,3,4])
    print bs.binarySearch(7)
    print bs.binarySearch(0)
    print bs.binarySearch(1)
    print bs.binarySearch(2)
    print bs.binarySearch(3)
    print bs.binarySearch(4)