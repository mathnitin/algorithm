#!/bin/python

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class
class LinkedList:
    # Function to initialize the Linked 
    # List object
    def __init__(self): 
        self.head = None
    
    # Insert a node in linkedList
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            curNode.next = node
    
    # Traverse a linkedList
    def traverse(self):
        curNode = self.head
        if self.head == None:
            return
        else:
            while curNode:
                print curNode.data, '-->',
                curNode = curNode.next

if __name__ == "__main__" :
    lList  = LinkedList()   # Create Linked list object
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    lList.insert(n1)
    lList.insert(n2)
    lList.insert(n3)
    lList.traverse()
