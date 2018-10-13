#!/bin/python

'''
First common Ancestor of Binary tree .

Given two nodes of a tree,
method should return the deepest common ancestor of those nodes.

         A
        / \
       B   C
      / \
     D   E
        / \
       G   F

 commonAncestor(D, F) = B
 commonAncestor(C, G) = A
 commonAncestor(E, B) = B
 commonAncestor(X, B) = None
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None
  
    def commonAncestor(self, node1, node2):
        curNode = self.root
        path1 = self.DFS(node1)
        path2 = self.DFS(node2)
        if len(path1) == 0 or len(path2) == 0:
            print "Common Ancestor is:", None
            return
        for index in range(min(len(path1), len(path2))):
            if path1[index] is not path2[index]:
                index = index - 1
                break
        print "Common Ancestor is:", path1[index].value

    def DFSutil(self, root, node, path):
        path.append(root)
        if root is node:
            return True
        if root.left:
            retVal = self.DFSutil(root.left, node, path)
            if retVal is True:
                return retVal
        if root.right:
            retVal = self.DFSutil(root.right, node, path)
            if retVal is True:
                return retVal
        path.remove(root)
        return False
        

    def DFS(self, node):
        path = []
        curNode = self.root
        self.DFSutil(curNode, node, path)
        return path
            


if __name__ == "__main__":
    tree = BinaryTree()
    nA = Node('A')
    nB = Node('B')
    nC = Node('C')
    nD = Node('D')
    nE = Node('E')
    nF = Node('F')
    nG = Node('G')
    nX = Node('X')
    tree.root = nA
    nA.left = nB
    nA.right = nC
    nB.left = nD
    nB.right = nE
    nE.left = nG
    nE.right = nF
    # B
    tree.commonAncestor(nD, nF)
    # A
    tree.commonAncestor(nC, nG)
    # B
    tree.commonAncestor(nE, nB)
    # None
    tree.commonAncestor(nX, nB)

    