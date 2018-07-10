#!/bin/python

'''
Link list base class. Implement Singly link list and doubly link list using this. 

Also learn the concept of inheritence. 
'''

class LinkList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def traverse(self):
        if self.head is None:
            print "Empty List"
            return
        print self.head.data, 
        if self.head.next == None:
            print 
            return
        else:
            curNode = self.head.next
            while curNode:
                print '-->' , curNode.data,
                curNode = curNode.next
        print 

    def size(self):
        return count