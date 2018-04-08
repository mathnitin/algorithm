#!/bin/python

'''
Find the maximum height of the tree
'''

class Node(self):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(self):
    def __init__(self):
        self.root = None

    def addNode(self, data, rootNode):
        if rootNode == None:
            node = Node(data)
            self.root = node
        if data > rootNode.data:
            if rootNode.right != None:
                self.addNode(data, rootNode.right)
            else:
                node = Node(data)
                rootNode.right = node
        if data <= rootNode.data:
            if rootNode.left != None:
                self.addNode(data, rootNode.left)
            else:
                node = Node(data)
                rootNode.left = node
            
    