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

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find_minimum_value(self):
        if self.left:
            return self.left.find_minimum_value()
        else:
            return self.value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        n = Node(value)
        if self.root == None:
            self.root = n
        else:
            node = self.root
            parent = self.root
            while node != None:
                parent = node
                if value <= node.value:
                    node = node.left
                else:
                    node = node.right
            if value <= parent.value:
                parent.left = n
            else:
                parent.right = n

    def search(self, value, node):
        if node == None:
            return Node("null")
        elif node.value == value:
            return node
        else:
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            return self.search(value, node)

    def delete(self, value, node, parent=None):
        if node.value == value:
            # Case 1 - Left and right child both doesn't exists.
            if node.left is None and node.right is None:
                if parent is None:
                    node = None
                elif parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                return True
            # Case 2 - Right child exists.
            elif node.left is None:
                if parent is None:
                    node = node.right
                elif parent.left is node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return True
            # Case 2 - Left child exists.
            elif node.right is None:
                if parent is None:
                    node = node.left
                elif parent.left is node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return True
            # Case 3 - Left and Right child both exists.
            else:
                node.value = node.right.find_minimum_value()
                return self.delete(node.value, node.right, node)
        elif value < node.value and node.left:
            return self.delete(value, node.left, node)
        elif value < node.value:
            return False
        elif value > node.value and node.right:
            return self.delete(value, node.right, node)
        elif value > node.value:
            return False

    # left sub-tree, root, right sub-tree
    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print node.value, 
            self.inOrder(node.right)

    # root, left sub-tree, right sub-tree
    def preOrder(self, node):
        if node:
            print node.value, 
            self.preOrder(node.left)
            self.preOrder(node.right)

    #left sub-tree, right sub-tree, root
    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print node.value,

    def breadthFirst(self, node):
        if node:
            if node.left:
                print node.left.value,
            if node.right:
                print node.right.value, 
            self.breadthFirst(node.left)
            self.breadthFirst(node.right)

    def deapthFirst(self, node):
        if node:
            print node.value,
            self.deapthFirst(node.left)
            self.deapthFirst(node.right)


if __name__=="__main__":
    tree = BinarySearchTree()
    arr = [4,3,5,1,2,6,7]
    for val in arr:
        tree.insert(val)
    node = tree.search(3, tree.root)
    print node.value
    node = tree.search(11, tree.root)
    print node.value
    print 'Breath First or Level Order:'
    print tree.root.value,
    tree.breadthFirst(tree.root)
    print '\nDeapth First:'
    tree.deapthFirst(tree.root)
    print '\nPre order:'
    tree.preOrder(tree.root)
    print '\nIn order:'
    tree.inOrder(tree.root)
    print '\nPost order:'
    tree.postOrder(tree.root)
    print '\nDelete non-existing value (10)'
    print tree.delete(10,tree.root)
    print 'Delete existing value(7)'
    print tree.delete(7, tree.root)
    print 'In order (7):'
    tree.inOrder(tree.root)
    print 'Delete existing value(6)'
    print tree.delete(6, tree.root)
    print 'In order (6):'
    tree.inOrder(tree.root)
    print 'Delete existing value(3)'
    print tree.delete(3, tree.root)
    print 'In order (3):'
    tree.inOrder(tree.root)
    print 'Delete existing value(4)'
    print tree.delete(4, tree.root)
    print 'In order (4):'
    tree.inOrder(tree.root)
    print '\n\nNew Root:'
    print tree.root.value