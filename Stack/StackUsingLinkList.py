#!/bin/python

'''
Implement stack using linklist
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None
    
    def stackPush(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def stackPop(self):
        node = self.head
        self.head = self.head.next
        return node

    def stackPeek(self):
        return self.head

    def stackTraverse(self):
        curNode = self.head
        if self.head == None:
            return
        else:
            while curNode:
                print curNode.data,
                curNode = curNode.next

if __name__ == "__main__":
    stack = LinkList()
    stack.stackPush(Node(3))
    stack.stackPush(Node(4))
    stack.stackPush(Node(5))
    stack.stackPush(Node(6))
    print stack.stackTraverse()
    print stack.stackPeek().data
    print stack.stackPop().data
    #print stack.stackTraverse()