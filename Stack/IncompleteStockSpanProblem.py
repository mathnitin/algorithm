#!/bin/python

'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate 
span of stock's price for all n days. The span Si of the stock's price on a given day i is defined as the maximum number of 
consecutive days just before the given day' for which the price of the stock on the current day is less than or equal to its 
price on the given day.

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = 0
        self.output = 1

class Stack():
    def __init__(self):
        self.head = None
        self.stackIndex = 0
    
    def push(self, data):
        self.stackIndex += 1
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        node.index = self.stackIndex

    def pushNode(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.isEmpty() == True:
            return None
        elem = self.head
        self.head = self.head.next
        return elem

    def peek(self):
        if self.isEmpty() == True:
            return None
        return self.head.data        

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

def printNode(node):
    pass
#    print "data: ", node.data
#    print "index: ", node.index
#    print "output: ", node.output


if __name__ == "__main__":
    inputStack = Stack()
    inputStack.push(100)
    inputStack.push(80)
    inputStack.push(60)
    inputStack.push(70)
    inputStack.push(60)
    inputStack.push(75)
    inputStack.push(85)

    prevElemStack = Stack()
    while inputStack.isEmpty() != True:
        tempStack = Stack()
        curElem = inputStack.pop()
        print "Cur Elem: "
        printNode(curElem)
        while prevElemStack.isEmpty() != True:
            prevElem = prevElemStack.pop()
            print "prev elem: "
            printNode(prevtNode)
            curElem.output = curElem.index - prevElem.index
            if prevElem.data > curElem.data:
                print "prevElem.data > curElem.data", prevElem.data, curElem.data
                print "break"
                break
            else:
                print "pushNode: prevElem to tempStack"
                tempStack.pushNode(prevElem)
        while tempStack.isEmpty() != True:
            tempElem = tempStack.pop()
            print "Temp Elem:"
            printNode(tempElem)
            prevElemStack.pushNode(tempElem)

    print "Output: ",
    while prevElemStack.isEmpty() != True:
        print prevElemStack.pop().output, 


