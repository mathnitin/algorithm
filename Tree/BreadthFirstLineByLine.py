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

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def __printHandler(self, curLevel):
        if len(curLevel) == 0:
            return
        nextLevel = []
        while curLevel:
            curElem = curLevel[0]
            del curLevel[0]
            if curElem.left:
                nextLevel.append(curElem.left)
            if curElem.right:
                nextLevel.append(curElem.right)
            print curElem.data,
        self.__printHandler(nextLevel)
        
    def breadthFirstTraversalLineByLine(self):
        #Write code Here
        curLevel = []
        curLevel.append(self.root)
        self.__printHandler(curLevel)

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
