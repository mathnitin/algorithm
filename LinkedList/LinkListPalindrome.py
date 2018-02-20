#!/bin/python

'''
Function to check if a singly linked list is palindrome
3.2
Given a singly linked list of characters, write a function that returns true if the given list is palindrome, else false.

N--I--T--I--N
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkList():
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        if self.head == None :
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next

def IsListPalindrome(lList):
    if lList == None:
        return False
    if lList.head.next == None:
        return True
    # Find mid pointer of the link list
    prevP = midP = fastP = lList.head
    while fastP != None and fastP.next != None:
        prevP = midP
        midP = midP.next
        fastP = fastP.next.next
    # Print mid corrector and last corrector here. 
    # print midP.data, fastP.data, prevP.data
    # Reverse the list from midP to fastP
    prevP.next = None
    lList2 = LinkList()
    lList2.head = midP
#    print "Print 1st part of list."
#    lList.traverse()
#    print "\n"
    reverse(lList2)
    node1 = lList.head
    node2 = lList2.head
    while node1 and node2:
        if node1.data == node2.data:
            node1 = node1.next
            node2 = node2.next
        else:
            reverse(lList2)
            prevP.next = lList2.head
            return False
    if node1:
        if node1.next != None:
            reverse(lList2)
            prevP.next = lList2.head
            return False
    if node2:
        if node2.next != None:
            reverse(lList2)
            prevP.next = lList2.head
            return False
    reverse(lList2)
    prevP.next = lList2.head
    return True
    

def reverse(lList2):
    stP = lList2.head
    nextP = stP.next
    stP.next= None
    while nextP.next:
        temp = nextP.next
        nextP.next = stP
        stP = nextP
        if temp:
            nextP = temp
    nextP.next = stP
    lList2.head = nextP
#    print "Print 2nd part of list."
#    lList2.traverse()


if __name__ == "__main__":
    n1 = Node("N")
    n2 = Node("I")
    n3 = Node("T")
    n4 = Node("I")
    n5 = Node("N")
    string = LinkList()
    string.insert(n1)
    string.insert(n2)
    string.insert(n3)
    string.insert(n4)
    string.insert(n5)
 #   print "Original list: "
 #   string.traverse()
 #   print "\n"
    print IsListPalindrome(string)
    print "The input string was:"
    string.traverse()