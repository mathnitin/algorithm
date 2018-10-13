#!/bin/python
'''
Implement Priority Queue using max heap.

'''

class Node():
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value


class PriorityQueue():
    def __init__(self):
        self.priorityQueue = []

    @property
    def size(self):
        return len(self.priorityQueue)

    def insert(self, value, priority):
        node = Node(value, priority)
        self.priorityQueue.append(node)
        index = self.size
        self._reverse_heapify(index)

    def update(self, value, priority):
        pass

    def deleteValue(self, value, priority):
        pass

    def deleteIndex(self, index):
        pass

    def search(self, value, priority):
        pIndex = 0
        cIndex1 = 2*pIndex + 1
        cIndex2 = 2*pIndex + 2
        while pIndex < self.size:
            node = self.priorityQueue[pIndex]
            if priority <  

    def getMax(self):
        if self.size == 0:
            return None
        return self.priorityQueue[0]

    def _reverse_heapify(self, curIndex):
        parentIndex = (curIndex-1)/2
        while parentIndex > 0:
            if self.priorityQueue[parentIndex].priority > self.priorityQueue[curIndex].priority:
                self.priorityQueue[parentIndex], self.priorityQueue[curIndex] =  self.priorityQueue[curIndex], self.priorityQueue[parentIndex]
                curIndex = parentIndex
            else:
                break


if __name__ == "__main__":
    print "Test priority queue"