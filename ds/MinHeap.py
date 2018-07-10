#!/bin/python

'''
Implementation of Min heap. 

A Binary Heap is a Binary Tree with following properties.
1) It's a complete tree (All levels are completely filled except possibly the last level and the last level has all keys 
as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys 
present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar 
to MinHeap.
'''

class MinHeap:
    def __init__(self):
        self._items = []

    @property
    def size(self):
        return len(self._items)

    def _heapify(self, index):
        if index > self.size-1:
            return
        childIndex1 = 2*index + 1
        childIndex2 = 2*index + 2
        smallerChildIndex = None
        # Find the smallest child.
        if childIndex1 >= self.size:
            smallerChildIndex = None
        elif childIndex2 >= self.size:
             smallerChildIndex = childIndex1
        elif self._items[childIndex1] <= self._items[childIndex2]:
            smallerChildIndex = childIndex1
        elif self._items[childIndex2] <= self._items[childIndex1]:
            smallerChildIndex = childIndex2
        # Compare values    
        if smallerChildIndex != None and self._items[index] > self._items[smallerChildIndex]:
            self._items[index], self._items[smallerChildIndex] = self._items[smallerChildIndex], self._items[index]
            self._heapify(smallerChildIndex)

    def _reverse_heapify(self, index):
        parentIndex = (index - 1)/2
        if parentIndex < 0:
            return
        if self._items[parentIndex] > self._items[index]:
            self._items[parentIndex], self._items[index] = self._items[index], self._items[parentIndex]
            self._reverse_heapify(parentIndex)
        return

    def getMin(self):
        if self.size != 0:
            return self._items[0]
        return None

    def extractMin(self):
        if self.size == 0:
            return None
        elem = self._items[0]
        self._items[0] = self._items.pop()
        self._heapify(0)
        return elem

    def decreaseKey(self, index, new_val):
        self._items[index] = new_val
        self._reverse_heapify(index)

    def insertKey(self, value):
        self._items.append(value)
        self._reverse_heapify((self.size-1))

    def deleteKey(self, index):
        self.decreaseKey(index, float("-inf"))
        self.extractMin() 


if __name__ == "__main__":
    # Driver pgoratm to test above function
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.deleteKey(1)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
 
    print heapObj.extractMin(),
    print heapObj.getMin(),
    heapObj.decreaseKey(2, 1)
    print heapObj.getMin(),
