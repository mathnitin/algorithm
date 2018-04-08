#!/bin/python

'''
Stack implementation using array
'''

class Stack:
    def __init__(self):
        self.stack = []

    def stackPush(self, data):
        self.stack.append(data)

    def stackPop(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        return self.stack.pop()

    def stackPeek(self):
        return self.stack[0]

    def stackTraverse(self):
        return self.stack

if __name__ == "__main__":
    stack = Stack()
    stack.stackPush(3)
    stack.stackPush(4)
    stack.stackPush(5)
    stack.stackPush(6)
    print stack.stackTraverse()
    print stack.stackPeek()
    print stack.stackPop()
    print stack.stackTraverse()