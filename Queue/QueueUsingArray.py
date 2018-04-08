#!/bin/python

'''
Implement Queue using a list
'''

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0,data)

    def dequeue(self):
        if self.isEmpty() == True:
            return None
        return self.queue.pop()

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def traverse(self):
        for i in reversed(self.queue):
            print i, 

    def peek(self):
        elem = self.dequeue()
        self.queue.append(elem)
        return elem

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print "First elem: ", queue.peek()
    print "Traverse: ", queue.traverse()
    print "Dequeue elem: ", queue.dequeue()
    print "Dequeue elem: ", queue.dequeue()
    print "Dequeue elem: ", queue.dequeue()
    print "Dequeue elem: ", queue.dequeue()
    print "Dequeue elem: ", queue.dequeue()
    print "Is queue empty: ", queue.isEmpty()
    print "Dequeue elem: ", queue.dequeue()

