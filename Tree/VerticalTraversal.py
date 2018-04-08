#!/bin/python

'''
Following are the generally used ways for traversing trees.

            1
           /  \   
          2     3    
        /  \   /  \       
       4   5  6    7

Vertical Traversal
4
2
1 5 6
3
7
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

    def verticalTraversal(self, levelDict, node, level=0):
        if node is None:
            return
        levelDict[level].append(node.data)
        self.verticalTraversal(levelDict, node.left, level-1)
        self.verticalTraversal(levelDict, node.right, level+1)

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
    levelDict = defaultdict(list)
    tree.verticalTraversal(levelDict, tree.root)
    od = OrderedDict(sorted(levelDict.items()))
    print "Vertical Traversal:"
    for k, v in od.iteritems():
        print v