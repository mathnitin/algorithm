#!/bin/python

'''

'''

from LinkList import *


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkList(LinkList):
    
    def insert_first(self, data):
        _node = Node(data)
        if self.head is None:
            self.head = self.tail = _node
            return
        _node.next = self.head
        self.head.prev = _node
        self.head = _node
    
    def insert_end(self, data):
        _node = Node(data)
        if self.head is None:
            self.head = self.tail = _node
            return
        self.tail.next = _node
        _node.prev = self.tail
        self.tail = _node


    def delete_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            _node = self.head
            self.head = None
            return _node.data
        _node = self.head
        self.head.next.prev = None
        self.head = self.head.next
        _node.next = None
        return _node.data


    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            _node = self.head
            self.head = None
            return _node.data 
        _node = self.tail 
        self.tail = self.tail.prev
        self.tail.next = None 
        _node.prev = None 
        return _node.data

    
if __name__ == "__main__":
    dl = DoublyLinkList()
    dl.insert_first(1)
    dl.insert_end(2)
    dl.insert_end(3)
    dl.traverse()
    dl.delete_first()
    dl.traverse()
    dl.delete_end()
    dl.traverse()
    dl.delete_first()
    dl.traverse()