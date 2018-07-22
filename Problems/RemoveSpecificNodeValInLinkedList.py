#!/bin/python

'''
Remove all nodes in a link list with specific value.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            tempNode = self.head
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = node

    def traverse(self):
        tempNode = self.head
        while tempNode != None:
            print tempNode.data, 
            tempNode = tempNode.next

def removeNode(list, value):
    while list.head.next != None:
        if list.head.data != value:
            break
        else:
            list.head = list.head.next
    tempNode = list.head
    while tempNode.next != None:
        if tempNode.next.data == value:
            tempNode.next = tempNode.next.next
        else:
            tempNode = tempNode.next

if __name__ == "__main__":
    llist = LinkList()
    llist.insert(3)
    llist.insert(2)
    llist.insert(1)
    llist.insert(3)
    llist.insert(3)
    llist.insert(3)
    llist.insert(3)
    llist.insert(5)
    llist.insert(4)
    llist.insert(3)
    llist.insert(3)
    llist.traverse()
    print
    removeNode(llist, 3)
    llist.traverse()