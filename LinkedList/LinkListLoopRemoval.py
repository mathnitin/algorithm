#!/bin/python

'''
Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop is present,
then removes the loop and returns true. And if the list doesn't contain loop then returns false. 
Below diagram shows a linked list with a loop. detectAndRemoveLoop() must change the below list to 1->2->3->4->5->NULL.

1 --- 2 --- 3
      |     |
      5 --- 4
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.nodeVisited = False
    
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

def detectAndRemoveLoop(node):
    curNode = node
    curNode.nodeVisited = True
    node = curNode.next
    while node.next != None and node.nodeVisited != True:
        node.nodeVisited = True
        curNode = node
        node = node.next
    if node.nodeVisited == True:
        curNode.next = None
        return True
    else:
        return False


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    list1 = LinkList()
    list1.insert(n1)
    list1.insert(n2)
    list1.insert(n3)
    list1.insert(n4)
    list1.insert(n5)
    n5.next = n2
    result = detectAndRemoveLoop(list1.head)
    print result
    print list1.traverse()