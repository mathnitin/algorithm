#!/bin/python

'''
LRU Cache Implementation

How to implement LRU caching scheme? What data structures should be used?
We are given total possible page numbers that can be referred. We are also given cache (or memory) size 
(Number of page frames that cache can hold at a time). The LRU caching scheme is to remove the least recently 
used frame when the cache is full and a new page is referenced which is not there in cache. Please see the Galvin 
book for more details (see the LRU page replacement slide here).

We use two data structures to implement an LRU Cache.

Queue which is implemented using a doubly linked list. The maximum size of the queue will be equal to the total number 
of frames available (cache size).The most recently used pages will be near front end and least recently pages will be 
near rear end.
A Hash with page number as key and address of the corresponding queue node as value.
When a page is referenced, the required page may be in the memory. If it is in the memory, we need to detach the node of 
the list and bring it to the front of the queue.
If the required page is not in the memory, we bring that in memory. In simple words, we add a new node to the front of 
the queue and update the corresponding node address in the hash. If the queue is full, i.e. all the frames are full, we 
remove a node from the rear of queue, and add the new node to the front of queue.

Example - Consider the following reference string:

1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Find the number of page faults using least recently used (LRU) page replacement algorithm with 3 page frames.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue(object):
    def __init__(self, maxSize):
        self.curElemCount = 0
        self.head = None
        self.tail = None
        self.dict = {}
        self.maxSize = maxSize

    def enqueue(self, data):
        node = Node(data)
        # First entry in the queue
        if self.head == None:
            self.curElemCount += 1
            self.head = self.tail = node
            self.dict[data] = node
            return
        else:
            # The data exists in the dict. move the node to top.
            if self.dict.has_key(data):
                # Fetch the node info from dict.
                curNode = self.dict[data]
                prevNode = curNode.left
                nextNode = curNode.right
                if prevNode != None:
                    prevNode.right = nextNode
                if nextNode != None:
                    nextNode.left = prevNode
                # Set new tail pointer
                if curNode.right == None:
                    self.tail = prevNode
                curNode.left = None
                curNode.right = self.head
                self.head.left = curNode
                self.head = curNode
            # Data does not exists in the dict.
            else:
                # if the queue has reached max size, dequeue an element
                if self.curElemCount == self.maxSize:
                    self.dequeue()
                node.right = self.head
                self.head.left = node
                self.head = node
                self.dict[data] = node
                self.curElemCount += 1

    def dequeue(self):
        if self.tail:
            # Remove the last element
            curElem = self.tail
            newTail = self.tail.left
            self.tail.left = None
            if newTail:
                newTail.right = None
            self.tail = newTail
            # Remove the cur element from the dictinoary. 
            del self.dict[curElem.data]
            # Reduce the size of the queue.
            self.curElemCount -= 1

    def traverse(self):
        curElem = self.head
        print "\n"
        while curElem:
            print curElem.data ,
            curElem = curElem.right

if __name__ == "__main__":
    q = Queue(3)
    # 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
    q.enqueue(1)
    q.traverse()
    q.enqueue(2)
    q.traverse()
    q.enqueue(3)
    q.traverse()
    q.enqueue(4)
    q.traverse()
    q.enqueue(1)
    q.traverse()
    q.enqueue(2)
    q.traverse()
    q.enqueue(5)
    q.traverse()
    q.enqueue(1)
    q.traverse()
    q.enqueue(2)
    q.traverse()
    q.enqueue(3)
    q.traverse()
    q.enqueue(4)
    q.traverse()
    q.enqueue(5)
    q.traverse()