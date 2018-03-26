#!/bin/python

'''
Implementation of Stack.

'''

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty:
            return self.stack.pop()
        return None

    @property
    def isEmpty(self):
        return self.stack == []

    def traverse(self):
        print self.stack
    
    def reverse(self):
        tempStack = Stack()
        while not self.isEmpty:
            tempStack.push(self.pop())
        return tempStack

    def peek(self):
        if not self.isEmpty:
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)