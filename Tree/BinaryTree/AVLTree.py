#!/bin/python


'''
Implement AVL Tree

https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def find_minimum_value(self):
        if self.left:
            return self.left.find_minimum_value()
        else:
            return self.value


class AVLTree():
    def insert(self, data, node):
        # Step 1 - Normal insert of the node.
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(data, node.left)
        else:
            node.right = self.insert(data, node.right)
    
        # Step 2 - Update the height
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 

        # Step 3 - Calculate balance factor
        balance = self.getBalanceFactor(node)

        # Step 4 - If the node is unbalanced, check which case it falls in.
        # Case 1 - Left left rotation
        if balance > 1 and data < node.left.data: 
            return self.rightRotate(node) 

        # Case 2 - Right right rotation
        if balance < -1 and data > node.right.data: 
            return self.leftRotate(node)
        
        # Case 3 - Left Right rotation
        if balance > 1 and data > node.left.data: 
            node.left = self.leftRotate(node.left) 
            return self.rightRotate(node) 

        # Case 4 - Right Left rotation
        if balance < -1 and data < node.right.data: 
            node.right = self.rightRotate(node.right) 
            return self.leftRotate(node) 

        return node

    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.data: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.data: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalanceFactor(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalanceFactor(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalanceFactor(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalanceFactor(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalanceFactor(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    def rightRotate(self, root):
        # Fetch required pointers
        leftChild = root.left
        leftRightChild  = leftChild.right
        # Rotate.
        root.left = leftRightChild
        leftChild.right = root
        # Get height.
        root.height = 1 + max (self.getHeight(root.right), self.getHeight(root.left))
        leftChild.height = 1 + max(self.getHeight(leftChild.left), self.getHeight(leftChild.right))
        # Return
        return leftChild

    def leftRotate(self, root):
        # Fetch required pointers
        rightChild = root.right
        rightleftChild  = rightChild.left
        # Rotate.
        root.right = rightleftChild
        rightChild.left = root
        # Get height.
        root.height = 1 + max (self.getHeight(root.right), self.getHeight(root.left))
        rightChild.height = 1 + max(self.getHeight(rightChild.left), self.getHeight(rightChild.right))
        # Return
        return rightChild

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
        
    # left sub-tree, root, right sub-tree
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print node.data, 
            self.inOrder(node.right)


if __name__ == "__main__":
    # Driver program to test above function 
    myTree = AVLTree() 
    root = None
    root = myTree.insert(10, root) 
    root = myTree.insert(20, root) 
    root = myTree.insert(30, root) 
    root = myTree.insert(40, root) 
    root = myTree.insert(50, root) 
    root = myTree.insert(25, root) 
    myTree.inOrder(root)
    root = myTree.delete(root, 22)
    print 
    myTree.inOrder(root)