#!/bin/python

'''
Following are the generally used ways for traversing trees.

            1
           /  \   
          2     3    
        /  \   /  \       
       4   5  6    7

Breath First Traversal or Level Order Traversal Line by line
1
2 3
4 5 6 7
'''

from ds.Queue import Queue

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def __breadthFirstTraversalLineByLine(self, queue):
        newQueue = Queue()
        while not queue.isEmpty:
            elem = queue.dequeue()
            print elem.data,
            if elem.left:
                newQueue.enqueue(elem.left)
            if elem.right:
                newQueue.enqueue(elem.right)
        if not newQueue.isEmpty:
            print ""
            self.__breadthFirstTraversalLineByLine(newQueue)

    def breadthFirstTraversalLineByLine(self):
        tempNode = self.root
        if tempNode == None:
            return
        queue = Queue()
        queue.enqueue(tempNode)
        self.__breadthFirstTraversalLineByLine(queue)

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
    print "Breath First Traversal or Level Order Traversal Line by line:"
    tree.breadthFirstTraversalLineByLine()
