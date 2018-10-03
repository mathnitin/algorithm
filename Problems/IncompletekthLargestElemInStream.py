#!/bin/python

'''
K'th largest element in a stream
Given an infinite stream of integers, find the k'th largest element at any point of time.

Example:

Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output:    { _,  _, 10, 11, 20, 40, 50,  50, ...}
'''

class maxHeap:
    def __init__(self, maxSize):
        self.items = []
        self.maxSize = maxSize

    def getSize(self):
        return len(self.items) -1

    def getMaxVal(self):
        return self.items[0]

    def insertElem(self, elem):
        self.items.append(elem)
        self.reverseHeapify(self.getSize())

    def extractMax(self):
        elem = self.items[0]
        self.items.remove(elem)
        self.heapify(0)

    def reverseHeapify(self, index):
        parentIndex = (index-1)/2
        if parentIndex < 0:
            return
        if self.items[parentIndex] < self.items[index]:
            self.items[parentIndex], self.items[index] = self.items[index], self.items[parentIndex]
            self.reverseHeapify(parentIndex)
        return

    def heapify(self, index):
        childIndex1 = 2*index + 1
        childIndex1 = 2*index + 2
        smallIndex = None
        # Find the smallest child.
        if childIndex1 >= self.getSize():
            smallIndex = None
        elif childIndex2 >= self.getSize():
             smallIndex = childIndex1
        elif self.items[childIndex2] <= self.items[childIndex1]:
            smallIndex = childIndex2
        # Compare values    
        if smallIndex is not None and self.items[index] > self.items[smallIndex]:
            self.items[index], self.items[smallIndex] = self.items[smallIndex], self.items[index]
            self.heapify(smallIndex)

if __name__ == "__main__":
    output = []
    stream = [10, 20, 11, 70, 50, 40, 100, 5]
    k = 3
    mH = maxHeap(k)
    for i in stream:
        print "mH.getSize()+1", mH.getSize()+1
        print "mH.maxSize", mH.maxSize
        if (mH.getSize()+1) < mH.maxSize:
            mH.insertElem(i)
            output.append("_")
        else:
            if i < mH.getMaxVal():
                mH.extractMax()
                mH.insertElem(i)
            output.append(mH.getMaxVal())
    print output