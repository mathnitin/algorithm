#!/bin/python

'''
Implementation of Max heap. 

A Binary Heap is a Binary Tree with following properties.
1) It's a complete tree (All levels are completely filled except possibly the last level and the last level has all keys 
as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys 
present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar 
to MinHeap.
'''

class MaxHeap:
    def __init__(self):
        self._items = []
        
    @property
    def size(self):
        return len(self._items)

    def _heapify(self, index):
        if index > self.size:
            return
        parent = index
        child1 = 2*parent + 1
        child2 = 2*parent + 2
        maxIndex = None
        # Find maxIndex
        if child1 > self.size :
            maxIndex = None
        elif child2 > self.size:
            maxIndex = child1
        elif self._items[child1] > self._items[child2]:
            maxIndex = child1
        else:
            maxIndex= child2
        # Check if it needs to ne replaced.
        if maxIndex != None and self._items[index] < self._items[maxIndex]:
            self._items[maxIndex], self._items[index] = self._items[index], self._items[maxIndex]
            self._heapify(maxIndex)
        return

    def _reverse_heapify(self, index):
        parentIndex = (index - 1)/2
        if parentIndex < 0:
            return
        if self._items[parentIndex] < self._items[index]:
            self._items[parentIndex], self._items[index] = self._items[index], self._items[parentIndex]
            self._reverse_heapify(parentIndex)
        return

    def getMax(self):
        if self.size == 0:
            return None
        return self._items[0]

    def extractMax(self):
        if self.size == 0:
            return None
        elem = self._items[0]
        self._items[0] = self._items.pop()
        self._heapify(0)
        return elem

    def decreaseKey(self, index, new_val):
        self._items[index] = new_val
        self._reverse_heapify(index)
        return

    def insertKey(self, value):
        self._items.append(value)
        index = self.size - 1
        parent = (index - 1)/2
        while parent >= 0:
            if self._items[index] > self._items[parent]:
                self._items[index], self._items[parent] = self._items[parent], self._items[index]
                index = parent
                parent = (index - 1)/2
            else:
                return
        return

    def deleteKey(self, index):
        self.decreaseKey(index, float("inf"))
        self.extractMax()
        return

    def traverse(self):
        print self._items


if __name__ == "__main__":
    input = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    maxHeap = MaxHeap()
    for elem in input:
        maxHeap.insertKey(elem)
    print "Input: ", input
    print "Max Heap: ", maxHeap.traverse()

    print "Delete elem:", maxHeap.deleteKey(0)
    print "Max Heap after delete: ", maxHeap.traverse()