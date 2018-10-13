#!/bin/python

'''
Convert Binary Search Tree to sorted Doubly Link List. We can only change the target of pointers, but cannot create any new nodes.

         10
       /    \
      6     14
     / \   /  \
    4  8  12  16

    4=6=8=10=12=14=16
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
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

    def inOrderUtil(self, node, ans):
        if node is None:
            return
        self.inOrderUtil(node.left, ans)
        ans.append(node)
        self.inOrderUtil(node.right, ans)

    def inOrder(self):
        ans = []
        self.inOrderUtil(self.root, ans)
        return ans


if __name__ == "__main__":
    tree = BinarySearchTree()
    #4=6=8=10=12=14=16
    data = [4,6,8,10,12,14,16]
    for val in data:
        tree.insert(val)

    ans = tree.inOrder()
    if len(ans) == 0:
        exit(0)
    if len(ans) == 1:
        ans[0].left = ans.right = None
        exit(0)
    prevIndex = 0
    ans[prevIndex].left = None
    for index in range(1, len(ans)):
        ans[prevIndex].right = ans[index]
        ans[index].left = ans[prevIndex]
        prevIndex = index
    ans[prevIndex].right = None

    node = ans[0]
    while node:
        print node.value, 
        node = node.right
