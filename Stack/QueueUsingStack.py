#!/bin/python

'''
Implement queu using stack
'''

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0 :
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return None

    def traverse(self):
        return self.stack

class Queue():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        while self.s1.peek() != None:
            self.s2.push(self.s1.pop())
        data = self.s2.pop()
        while self.s2.peek() != None:
            self.s1.push(self.s2.pop())
        return data

    def peek(self):
        while self.s1.peek() != None:
            self.s2.push(self.s1.pop())
        data = self.s2.peek()
        while self.s2.peek() != None:
            self.s1.push(self.s2.pop())
        return data

    def traverse(self):
        while self.s1.peek() != None:
            self.s2.push(self.s1.pop())
        print self.s2.traverse()
        while self.s2.peek() != None:
            self.s1.push(self.s2.pop())

if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print q1.traverse()
    print q1.peek()
    print q1.dequeue()
    print q1.traverse()   