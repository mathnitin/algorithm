#!/bin/python

'''
Sliding Window Maximum (Maximum of all subarrays of size k)
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples:

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90
'''

class Queue():
    def __init__(self):
        self.items = []
        self.isEmpty = True

    def enqueue(self, data):
        self.items.append(data)
        self.isEmpty = False

    def dequeue(self):
        if len(self.items) == 0:
            self.isEmpty = True
            return
        data = self.items[0]
        del self.items[0]
        return data

def slidingWindowMax(queue, window):
    outputQueue = Queue()
    tempQueue = Queue()
    curCount = 0
    maxVal = None
    while not queue.isEmpty and curCount < window:
        elem = queue.dequeue()
        if elem is None:
            break
        if maxVal < elem:
            maxVal = elem
        tempQueue.enqueue(elem)
        curCount += 1
        if curCount == window:
            if maxVal is None:
                maxVal = max(tempQueue.items)
            outputQueue.enqueue(maxVal)
            elem = tempQueue.dequeue()
            if elem == maxVal:
                maxVal = None
            curCount -= 1
    return outputQueue

if __name__ == "__main__":
    inputQueue = Queue()
    input = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    for i in input:
        inputQueue.enqueue(i)

    print inputQueue.items
    print "+++++"
    Output = slidingWindowMax(inputQueue, 4)
    print Output.items

