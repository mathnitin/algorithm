#!/bin/python

'''
Implementation of Queue.

'''

from ds.Stack import Stack
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.isEmpty:
            elem = self.queue[0]
            del self.queue[0]
            return elem
        return None

    @property
    def isEmpty(self):
        return self.queue == []

    def traverse(self):
        print self.queue
    
    def reverse(self):
        stack = Stack()
        tempQueue = Queue()
        while not self.isEmpty:
            stack.push(self.dequeue())
        while not stack.isEmpty:
            tempQueue.enqueue(stack.pop())
        return tempQueue 

    def peek(self):
        if not self.isEmpty:
            return self.queue[0]
        return None

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.traverse()
    revQ = q.reverse()
    revQ.traverse()