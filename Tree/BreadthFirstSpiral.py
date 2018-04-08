#!/bin/python

'''
Following are the generally used ways for traversing trees.

            1
           /  \   
          2     3    
        /  \   /  \       
       4   5  6    7

Breath First Traversal or Level Order Traversal Spiral Line by line
1
3 2
4 5 6 7

'''

from ds.Stack import Stack
from ds.Queue import Queue
from collections import defaultdict, OrderedDict

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def __breadthFirstTraversalSpiral(self, stack, flag):
        newStack = Stack()
        while not stack.isEmpty:
            elem = stack.pop()
            print elem.data,
            if flag is False:
                if elem.left:
                    newStack.push(elem.left)
                if elem.right:
                    newStack.push(elem.right)
            else:
                if elem.right:
                    newStack.push(elem.right)
                if elem.left:
                    newStack.push(elem.left)
        if not newStack.isEmpty:
            print ""
            self.__breadthFirstTraversalSpiral(newStack, not flag)

    def breadthFirstTraversalSpiral(self):
        tempNode = self.root
        if tempNode == None:
            return
        stack = Stack()
        stack.push(tempNode)
        self.__breadthFirstTraversalSpiral(stack, False)


if __name__=="__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left = n2
    n1.right= n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    tree = Tree(n1)
    print "Breath First Traversal or Level Order Traversal Spiral Line by line:"
    tree.breadthFirstTraversalSpiral()