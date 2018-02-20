#!/bin/python

'''
Reverse a linked list

Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing links between nodes.

Examples:

Input : Head of following linked list  
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

Input : Head of following linked list  
       1->2->3->4->5->NULL
Output : Linked list should be changed to,
       5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL
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
            while temp.next:
                temp = temp.next
            temp.next = node

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data, 
            temp = temp.next

    def reversal(self):
        if self.head.next == None:
            return
        prevNode = self.head
        curNode = prevNode.next
        prevNode.next = None
        while curNode.next:
            tempNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            if tempNode:
                curNode = tempNode
        curNode.next = prevNode
        self.head = curNode 

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    list = LinkList()
    list.insert(n1)
    list.insert(n2)
    list.insert(n3)
    list.insert(n4)
    print 'Original list:'
    list.traverse()
    list.reversal()
    print '\nReversed list:'
    list.traverse()