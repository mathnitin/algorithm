#!/bin/python

'''
Implement queue using link list.
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
        
    def dequeue(self):
        if self.head == None:
            return None
        if self.head.next == None:
            node = self.head
            self.head = None
            return node.data
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        node = temp.next
        temp.next = None
        return node.data

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def traverse(self):
        temp = self.head
        while temp != None:
            print temp.data, 
            temp = temp.next

    def peek(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp.data

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