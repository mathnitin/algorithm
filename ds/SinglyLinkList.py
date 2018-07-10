#!/bin/python

'''
Singly linked list.
'''

from LinkList import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkList(LinkList):

    def insert_first(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1


    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1


    def delete_first(self):
        if self.head is None:
            return
        else:
            data = self.head
            self.head = self.head.next
            self.count -= 1
            return data


    def delete_end(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            self.count -= 1
            return data
        else:
            curNode = self.head
            while curNode.next.next is not None:
                curNode = curNode.next
            data = curNode.next.data
            curNode.next = None
            self.count -= 1
            self.tail = curNode
            return data

    
    def reverse(self):
        if self.head.next is None:
            return 
        node = self.head.next
        self.head.next = None
        prevNode = self.head
        nextNode = node.next
        while nextNode is not None:
            node.next = prevNode
            prevNode = node
            node = nextNode
            nextNode = node.next
        node.next = prevNode
        self.head = node


if __name__ == "__main__":
    sl = SinglyLinkList()
    sl.insert_first(1)
    sl.insert_end(2)
    sl.insert_end(3)
    sl.traverse()
    sl.reverse()
    sl.traverse()
    sl.delete_first()
    sl.traverse()
    sl.delete_end()
    sl.traverse()
