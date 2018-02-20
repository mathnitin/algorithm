#!/bin/python

'''
Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, 
and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. 
The new list should be made by splicing together the nodes of the first two lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, 
then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

There are many cases to deal with: either 'a' or 'b' may be empty, during processing either 'a' or 'b' may run out first, 
and finally there's the problem of starting the result list empty, and building it up while going through 'a' and 'b'.
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

    def SortedMerge(self, l1, l2):
        list1 = l1.head
        list2 = l2.head
        resultList = LinkList()
        while list1 and list2:
            if list1.data <= list2.data:
                resultList.insert(Node(list1.data))
                list1 = list1.next
            else:
                resultList.insert(Node(list2.data))
                list2 = list2.next
        if list2:
            while list2:
                resultList.insert(Node(list2.data))
                list2 = list2.next
        if list1:
            while list1:
                resultList.insert(Node(list1.data))
                list1 = list1.next
        return resultList

# Function to merge two sorted linked list.
def mergeLists(head1, head2):
 
    # create a temp node NULL
    temp = None
 
    # List1 is empty then return List2
    if head1 is None:
        return head2
 
    # if List2 is empty then return List1
    if head2 is None:
        return head1
 
    # If List1's data is smaller or
    # equal to List2's data
    if head1.data <= head2.data:
 
        # assign temp to List1's data
        temp = head1
 
        # Again check List1's data is smaller or equal List2's 
        # data and call mergeLists function.
        temp.next = mergeLists(head1.next, head2)
         
    else:
        # If List2's data is greater than or equal List1's 
        # data assign temp to head2
        temp = head2
 
        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeLists(head1, head2.next)
 
    # return the temp list.
    return temp

if __name__ == "__main__":
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(15)
    n4 = Node(2)
    n5 = Node(3)
    n6 = Node(11)
    n7 = Node(20)
    list1 = LinkList()
    list1.insert(n1)
    list1.insert(n2)
    list1.insert(n3)
    list2 = LinkList()
    list2.insert(n4)
    list2.insert(n5)
    list2.insert(n6)
    list2.insert(n7)
    print 'Original list 1:'
    list1.traverse()
    print '\nOriginal list 2:'
    list2.traverse()
    result = LinkList()
    result = result.SortedMerge(list1, list2)
    print '\nSorted Merge List:'
    result.traverse()
    print '\nSorted Merge List recursive:'
    res = LinkList()
    res.head = mergeLists(list1.head, list2.head)
    res.traverse()