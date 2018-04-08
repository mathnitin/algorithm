#!/bin/python

'''
Find the maximum height of the tree

Input:
      1
    /  \
   2    3
 /
4

Output: 3

Input:
                  1
               /      \
              2        3
           /   \      /  \ 
          4     5    6    7
                    /
                    8
Output: 4
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, node):
        self.root = node

def __findHeight(node):
    if node is None:
        return 0
    leftHeight = __findHeight(node.left)
    rightHeight = __findHeight(node.right)
    return max(leftHeight,rightHeight)+1

def findHeight(tree):
    rootNode = tree.root
    if rootNode is None:
        return 0
    return __findHeight(rootNode)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    tree = Tree(n1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    print "Tree Height: ", findHeight(tree)
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n6.left = n8
    print "Tree Height: ", findHeight(tree)