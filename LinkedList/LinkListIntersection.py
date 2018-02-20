#!/bin/python

'''
Write a function to get the intersection point of two Linked Lists.
2.5
There are two singly linked lists in a system. By some programming error the end node of one of the linked list got linked into the second list, forming a inverted Y shaped list. Write a program to get the point where two linked list merge.

    3
    |__6
       |__9      10
          |__15__|
              |
              30

Above diagram shows an example with two linked list having 15 as intersection point.
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

# Mark the node visited from list1.
# Walk list2 and check if the node is marked or not. 
# If marked node found return node, else return None.
def findInsertion(list1, list2):
    while list1:
        list1.nodeVisited = True
        list1 = list1.next
    while list2:
        if list2.nodeVisited == True:
            return list2
        list2 = list2.next

if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(6)
    n3 = Node(9)
    n4 = Node(10)
    n5 = Node(15)
    n6 = Node(30)
    list1 = LinkList()
    list2 = LinkList()
    list1.insert(n1)
    list1.insert(n2)
    list1.insert(n3)
    list1.insert(n5)
    list1.insert(n6)
    list2.insert(n4)
    list2.insert(n5)
    print "\nList 1:"
    list1.traverse()
    print "\nList 2:"
    list2.traverse()
    print "\n\n"
    intersectedNode = findInsertion(list1.head, list2.head)
    if intersectedNode:
        print "Intersected node data: ", intersectedNode.data