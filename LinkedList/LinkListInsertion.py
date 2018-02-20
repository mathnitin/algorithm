#!/bin/python

'''
methods to insert a new node in linked list are discussed. A node can be added in three ways
1) At the front of the linked list
2) After a given node.
3) At the end of the linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insertAfterNode(self, prev_node, new_node):
        if prev_node is None:
            print "The given previous node must inLinkedList."
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    # Traverse a linkedList
    def traverse(self):
        curNode = self.head
        if self.head == None:
            return
        else:
            while curNode:
                print curNode.data,
                curNode = curNode.next

if __name__ == "__main__":
    lList = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    print 'Output must be print 1'
    lList.insertAtFront(n1)
    lList.traverse()
    print '\nOutput must be print 1 3'
    lList.insertAtEnd(n3)
    lList.traverse()
    print '\nOutput must be print 1 2 3'
    print lList.insertAfterNode(n1,n2)
    lList.traverse()