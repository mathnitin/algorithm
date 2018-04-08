#!/bin/python

'''
How to implement a stack which will support following operations in O(1) time complexity?

1. push() which adds an element to the top of stack.
2. pop() which removes an element from top of stack.
3. findMiddle() which will return middle element of the stack.
4. deleteMiddle() which will delete the middle element.
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.prevNode = None
        self.nextNode = None

class Stack():
    def __init__(self):
        self.head = None
        self.numOfElem = 0
        self.middleIndex = 0
        self.middlePt = None


    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.middlePt = self.head
            self.middleIndex = 1
        else:
            self.head.prevNode = node
            node.nextNode = self.head
            self.head = node
        self.numOfElem += 1
        midIndex = self.numOfElem/2
        if midIndex == self.middleIndex:
            self.middlePt = self.middlePt.prevNode
        

    def pop(self):
        retNode = self.head
        self.head = self.head.nextNode
        self.head.prevNode = None
        self.numOfElem -= 1
        midIndex = self.numOfElem/2
        if midIndex == self.middleIndex:
            self.middlePt = self.middlePt.nextNode


    def findMiddle(self):
        node = self.middlePt
        return node


    def deleteMiddle(self):
        retNode = self.middlePt
        prNode = self.middlePt.prevNode
        nxNode = self.middlePt.nextNode
        prNode.nextNode = nxNode
        nxNode.prevNode = prNode
        return retNode



if __name__ == "__main__":
    s = Stack()
    s.push(11)
    s.push(22)
    s.push(33)
    s.push(44)
    s.push(55)
    s.push(66)
    s.push(77)
    s.pop()
    s.pop()
    print s.findMiddle().data