#!/bin/python

'''
Following are the generally used ways for traversing trees.

            1
           /  \   
          2     3    
        /  \   /  \       
       4   5  6    7

Diagonal Traversal
1 3 7
2 5 6
4
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

    def __diagonalTraversal(self, queue):
        print ""
        if queue.isEmpty:
            return
        newQueue = Queue()
        while not queue.isEmpty:
            node = queue.dequeue()
            print node.data,
            if node.left:
                newQueue.enqueue(node.left)
            if node.right:
                print node.right.data,
                if node.right.left:
                    newQueue.enqueue(node.right.left)
        self.__diagonalTraversal(newQueue)

    def diagonalTraversal(self):
        tempNode = self.root
        if tempNode == None:
            return
        queue = Queue()
        while tempNode is not None:
            print tempNode.data,
            if tempNode.left:
                queue.enqueue(tempNode.left)
            tempNode = tempNode.right
        self.__diagonalTraversal(queue)

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
    print "Diagonal Traversal:"
    tree.diagonalTraversal()
