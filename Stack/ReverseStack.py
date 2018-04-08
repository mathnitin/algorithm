#!/bin/python

'''
Reverse a stack.

Examples:

Input :  1 2 3 4
Output : 4 3 2 1
'''

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        retun len(self.stack) == 0

def reverseStack(stack):
    tmp1 = Stack()
    while not stack.isEmpty():
        tmp1.push(stack.pop())
    return tmp1

if __name__ == "__main__":
    stack = Stack()
    inputData = [1, 2, 3, 4]
    for i in inputData:
        stack.push(i)
    print stack.stack
    output = reverseStack(stack)
    print output.stack