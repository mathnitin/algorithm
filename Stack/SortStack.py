#! /bin/python

'''
Sort a stack using recursion

Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. We can only use the following 
ADT functions on Stack S:
is_empty(S)  : Tests whether stack is empty or not.
push(S)         : Adds new element to the stack.
pop(S)         : Removes top element from the stack.
top(S)         : Returns value of the top element. Note that this
               function does not remove element from the stack.
Example:
Input:  -3  <--- Top
        14 
        18 
        -5 
        30 

Output: 30  <--- Top
        18 
        14 
        -3 
        -5 
'''

class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0 :
            return True
        return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def top(self):
        elem = self.stack.pop()
        self.push(elem)
        return elem

def sortStack(stack):
    if stack.is_empty() != True:
        elem = stack.pop()
        sortStack(stack)
        sortedInsert(stack, elem)

def sortedInsert(stack, elem):
    if stack.is_empty() == True or elem > stack.top():
        stack.push(elem)
    else:
        temp = stack.pop()
        sortedInsert(stack, elem)
        stack.push(temp)

if __name__ == "__main__":
    inputStack = Stack()
    

    inputStack.push(30)
    inputStack.push(-5)
    inputStack.push(18)
    inputStack.push(14)
    inputStack.push(-3)

    print "Input stack: "
    print inputStack.stack
    sortStack(inputStack)
    print "Output stack: "
    print inputStack.stack
