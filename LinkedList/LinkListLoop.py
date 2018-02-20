#!/bin/python

'''
Detect loop in a linked list
2.4
Given a linked list, check if the the linked list has loop or not. Below diagram shows a linked list with a loop.

1 -- 2 -- 3
     |    |
     5 -- 4
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

    def detectLoop(self):
        temp = self.head
        self.dictionary = {}
        while temp.next:
            if temp in self.dictionary:
                return True
            else:
                if temp:
                    self.dictionary[temp] = temp.data
            temp = temp.next
        return False

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
    # 'False'
    print '\n',list.detectLoop()
    # 'True'
    list.head.next.next.next.next = list.head
    print '\n',list.detectLoop()
