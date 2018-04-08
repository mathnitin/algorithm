#!/bin/python

'''
Design and Implement Special Stack Data Structure | Added Space Optimized Version

Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty() 
and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of 
SpecialStack must be O(1). 

Example:

Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should return 15, which is the minimum 
element in the current stack. 

If we do pop two times on stack, the stack becomes
29  --> TOP
19
18

When getMin() is called, it should return 18 which is the minimum 
in the current stack.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.minVal = None
        self.maxVal = None
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None
    
    def stackPush(self, node):
        if self.head == None:
            self.head = node
            node.minVal = node.maxVal = node.data
        else:
            node.next = self.head
            node.minVal = min(node.data, self.head.minVal)
            node.maxVal = max(node.data, self.head.maxVal)
            self.head = node
        
    def stackPop(self):
        node = self.head
        self.head = self.head.next
        return node

    def stackPeek(self):
        if self.head:
            return self.head
        return None

    def stackTraverse(self):
        curNode = self.head
        if self.head == None:
            return
        else:
            while curNode:
                print curNode.data,
                curNode = curNode.next

    def getMin(self):
        if self.stackPeek() != None:
            return self.stackPeek().minVal
        return None

    def getMax(self):
        if self.stackPeek() != None:
            return self.stackPeek().maxVal
        return None

if __name__ == "__main__":
    stack = LinkList()
    stack.stackPush(Node(16))
    stack.stackPush(Node(15))
    stack.stackPush(Node(29))
    stack.stackPush(Node(19))
    stack.stackPush(Node(18))
    print stack.stackTraverse()
    print stack.getMin()
    print stack.getMax()
    stack.stackPop()
    stack.stackPop()
    print stack.getMin()
    print stack.getMax()
    stack.stackPop()
    print stack.getMin()
    print stack.getMax()
    
    #print stack.stackTraverse()