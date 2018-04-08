#!/bin/python

'''
Following are the generally used ways for traversing trees.

            1
           /  \   
          2     3    
        /  \   /  \       
       4   5  6    7

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 6 3 7
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 6 7
(c) Postorder (Left, Right, Root) : 4 5 2 6 7 3 1

Breadth First or Level Order Traversal 
1 2 3 4 5 6 7
'''

from ds.Stack import Stack
from ds.Queue import Queue

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def __breadthFirstTraversal(self, node):
        if node.left is not None:
            print node.left.data,
        if node.right is not None:
            print node.right.data,
        if node.left is not None:
            self.__breadthFirstTraversal(node.left)
        if node.right is not None:
            self.__breadthFirstTraversal(node.right)

    def breadthFirstTraversal(self):
        tempNode = self.root
        if tempNode == None:
            return
        print tempNode.data,
        self.__breadthFirstTraversal(tempNode)

    def __preOrderTraversal(self, node):
        if node is not None:
            print node.data,
        if node.left is not None:
            self.__preOrderTraversal(node.left)
        if node.right is not None:
            self.__preOrderTraversal(node.right)

    def preOrderTraversal(self):
        tempNode = self.root
        if tempNode == None:
            return
        self.__preOrderTraversal(tempNode)

    def __postOrderTraversal(self, node, stack):
        if node:
            if node.left:
                stack.push(node.left)
                self.__postOrderTraversal(node.left, stack)
            if node.right:
                stack.push(node.right)
                self.__postOrderTraversal(node.right, stack)
            print node.data,
    
    def postOrderTraversal(self):
        tempNode = self.root
        if tempNode == None:
            return
        stack = Stack()
        self.__postOrderTraversal(tempNode, stack)

    def __inOrderTraversal(self, node, stack):
        if node:
            if node.left:
                stack.push(node.left)
                self.__inOrderTraversal(node.left, stack)
            print node.data,
            if node.right:
                stack.push(node.right)
                self.__inOrderTraversal(node.right, stack)
    
    def inOrderTraversal(self):
        tempNode = self.root
        if tempNode == None:
            return
        stack = Stack()
        self.__inOrderTraversal(tempNode, stack)


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
    print 'Breath First Traversal or Level Order Traversal:'
    tree.breadthFirstTraversal()
    print '\nPre order traversal:'
    tree.preOrderTraversal()
    print '\nIn order traversal:'
    tree.inOrderTraversal()
    print '\nPost order traversal:'
    tree.postOrderTraversal()