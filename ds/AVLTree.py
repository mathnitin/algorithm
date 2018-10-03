#!/bin/python

'''
Implementation of Tree.

          4
       /     \
      3       5
     / \     / \
    1   2   6   7

'''

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.balanceFactor = 0
        self.leftChild = None
        self.rightChild = None

    def _inorder(self):
        if self.leftChild:
            self.leftChild._inorder()
        print self.value
        if self.rightChild
            self.rightChild._inorder()

    def _insert(self, value, parent=None):
        if value <= self.value and self.leftChild:
            self.balanceFactor += 1
            self.leftChild._insert(value, self)
        elif value <= self.value:
            node = Node(value, self)
            self.balanceFactor += 1
            self.leftChild = node
        elif value > self.value and self.rightChild:
            self.balanceFactor -= 1
            self.rightChild._insert(value, self)
        else:
            node = Node(value, self)
            self.balanceFactor -= 1
            self.rightChild = node
        # Move up the tree to hit the node which needs to be balanced. 
        curNode = self
        while curNode.parent is not None or curNode.parent.balanceFactor < 1 or curNode.parent.balanceFactor > -1:
            curNode = curNode.parent
        # Reached the root.
        if curNode is None:
            return


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            node = Node(value)
            self.root = node
        else:
            self.root._insert(value)
        return

    def delete(self, value):
        pass

    def search(self, value):
        pass

    # left sub-tree, root, right sub-tree
    def inOrder(self):
        if self.root is None:
            return
        else:
            self.root._inorder()