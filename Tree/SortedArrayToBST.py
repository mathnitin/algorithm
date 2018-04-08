#!/bin/python

'''
Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.

Examples:

Input:  Array {1, 2, 3}
Output: A Balanced BST
     2
   /  
  1    3 

Input: Array {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  
   2    4
 /
1
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def createBST(self, listData, startIndex, endIndex):
        if startIndex > endIndex:
            return
        midIndex = (startIndex+endIndex)/2
        node = Node(listData[midIndex])
        node.left = self.createBST(listData, startIndex, midIndex-1)
        node.right = self.createBST(listData, midIndex+1, endIndex)
        return node
        

    def traverse(self, node):
        if node is None:
            return
        print node.data,
        self.traverse(node.left)
        self.traverse(node.right)

if __name__ == "__main__":
    listData = [1,2,3]
    tree = Tree()
    tree.root = tree.createBST(listData, 0, (len(listData)-1))
    tree.traverse(tree.root)