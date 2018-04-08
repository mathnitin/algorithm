#!/bin/python

'''
Program for Page Replacement Algorithms | Set 2 (FIFO)
Prerequisite : Page Replacement Algorithms

In operating systems that use paging for memory management, page replacement algorithm are needed to decide which page needed 
to be replaced when new page comes in. Whenever a new page is referred and not present in memory, page fault occurs and 
Operating System replaces one of the existing pages with newly needed page. Different page replacement algorithms suggest 
different ways to decide which page to replace. The target for all algorithms is to reduce number of page faults.

First In First Out (FIFO) page replacement algorithm -
This is the simplest page replacement algorithm. In this algorithm, operating system keeps track of all pages in the memory in a 
queue, oldest page is in the front of the queue. When a page needs to be replaced page in the front of the queue is selected for 
removal.

Example -1. Consider page reference string 1, 3, 0, 3, 5, 6 and 3 page slots.

Initially all slots are empty, so when 1, 3, 0 came they are allocated to the empty slots -> 3 Page Faults.
when 3 comes, it is already in memory so -> 0 Page Faults.
Then 5 comes, it is not available in memory so it replaces the oldest page slot i.e 1. -> 1 Page Fault.
Finally 6 comes, it is also not available in memory so it replaces the oldest page slot i.e 3 -> 1 Page Fault.

So total page faults = 6.

Example -2. Consider the following reference string: 0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1.

Using FIFO page replacement algorithm -

    0   |   2   |   1   |   6   |   4   |   0   |   1   |   0   |   3   |   1   |   2   |   1
--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------
    0   |   0   |   0   |   0   |   4   |   4   |       |       |   4   |   4   |   2   |
        |   2   |   2   |   2   |   2   |   0   |       |  hit  |   0   |   0   |   0   |
        |       |   1   |   1   |   1   |   1   |  hit  |       |   3   |   3   |   3   |
        |       |       |   6   |   6   |   6   |       |       |   6   |   1   |   1   |  hit

So, total number of page faults = 9.

Given memory capacity (as number of pages it can hold) and a string representing pages to be referred, write a function to find 
number of page faults.
'''

class Queue():
    def __init__(self, maxSize):
        self.queue = []
        self.maxSize = maxSize
        self.oldestIndex = 0

    def enqueue(self, data):
        if data in self.queue:
            print "Data: ", data
            print "Queue: ", self.queue
            print "    hit"
            return False
        curOldexIndex = self.dequeue()
        if curOldexIndex == None:
            self.queue.append(data)
        else:
            self.queue.insert(curOldexIndex, data)
        print "Data: ", data
        print "Queue: ", self.queue
        return True

    def dequeue(self):
        if len(self.queue) == self.maxSize:
            curOldestIndex = self.oldestIndex
            del self.queue[self.oldestIndex]
            self.oldestIndex += 1
            if self.oldestIndex == self.maxSize:
                self.oldestIndex = 0
            return curOldestIndex
        else:
            return None

if __name__ == "__main__":
    q = Queue(4)
    pageFault = 0
    entry = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
    for i in entry:
        if q.enqueue(i):
            pageFault += 1
    print pageFault