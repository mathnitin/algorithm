#!/bin/python

'''
Reverse a Linked List in groups of given size | Set 1
3.3
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
Output:  3->2->1->6->5->4->8->7->NULL. 

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL. 
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkList():
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def traverse(self):
        curNode = self.head
        while curNode:
            print curNode.data,
            curNode = curNode.next


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    list1 = LinkList()
    list1.insert(n1)
    list1.insert(n2)
    list1.insert(n3)
    list1.insert(n4)
    list1.insert(n5)
    list1.insert(n6)
    list1.insert(n7)
    list1.insert(n8)
    print 'Original List:'
    list1.traverse()