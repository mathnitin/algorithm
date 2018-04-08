#!/bin/python

'''
Implement Deque in python for below operations.

1.  append() :- This function is used to insert the value in its argument to the right end of deque.
2.  appendleft() :- This function is used to insert the value in its argument to the left end of deque.
3.  pop() :- This function is used to delete an argument from the right end of deque.
4.  popleft() :- This function is used to delete an argument from the left end of deque.
5.  index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, 
                            starting searching from beg till end index.
6.  insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
7.  remove(a) :- This function removes the first occurrence of value mentioned in arguments.
8.  count(a) :- This function counts the number of occurrences of value mentioned in arguments.
9.  extend(iterable) :- This function is used to add multiple values at the right end of deque. 
                       The argument passed is an iterable.
10. extendleft(iterable) :- This function is used to add multiple values at the left end of deque. 
                            The argument passed is an iterable. Order is reversed as a result of left appends.
11. getFront(): Gets the front item from deque.
12. getRear(): Gets the last item from deque.
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Deque():
    def __init__(self):
        self.lPointer = None
        self.rPointer = None

    def append(self, data):
        node = Node(data)
        if self.rPointer == None:
            self.lPointer = self.rPointer = node
        else:
            node.left = self.rPointer
            self.rPointer.right = node
            self.rPointer = node

    def appendleft(self, data):
        node = Node(data)
        if self.lPointer == None:
            self.lPointer= self.rPointer = node
        else:
            node.right = self.lPointer
            self.lPointer.left = node
            self.lPointer = node

    def pop(self):
        if self.rPointer == None:
            return None
        elem = self.rPointer
        self.rPointer = elem.left
        self.rPointer.right = None
        elem.left = elem.right = None
        return elem

    def popleft(self):
        if self.lPointer == None:
            return None
        elem = self.lPointer
        self.lPointer = elem.right
        self.lPointer.left = None
        elem.left = elem.right = None
        return elem

    def index(self, ele, beg, end):
        index = 0
        elem = self.lPointer
        # Walk to the beg index
        while elem != None and index <= beg:
            elem = elem.right
            index += 1
        # Check for ele from beg index to end index. 
        while elem != None and index <= end:
            if elem.data == ele:
                break 
            index += 1
            elem = elem.right
        if index <= end:
            return index
        else:
            return 0

    def insert(self, index, data):
        node = Node(data)
        i = 0
        elem = self.lPointer
        while elem.right != None:
            i += 1
            if i == index:
                node.right = elem.right
                node.left = elem
                elem.right = node
                return True
            elem = elem.right
        return False

    def remove(self, data):
        elem = self.lPointer
        if elem.data == data:
            self.lPointer = elem.right
            elem.right = None
            return
        while elem:
            if elem.data == data:
                lElem = elem.left
                rElem = elem.right
                lElem.right = rElem
                rElem.left = lElem
                return
            else:
                elem = elem.right

    def count(self, data):
        elem = self.lPointer
        count = 0
        while elem:
            if elem.data == data:
                count += 1
            elem = elem.right
        return count

    def extend(self, iterable):
        for i in iterable:
            node = Node(i)
            self.rPointer.right = node
            node.left = self.rPointer
            self.rPointer = node

    def extendleft(self, iterable):
        dq = Deque()
        for i in iterable:
            dq.append(i)
        dq.rPointer.right = self.lPointer
        self.lPointer.left = dq.rPointer
        self.lPointer = dq.lPointer

    def getFront(self):
        return self.lPointer.data

    def getRear(self):
        return self.rPointer.data

    def traverse(self):
        elem = self.lPointer
        while elem:
            print elem.data, 
            elem = elem.right

    def empty(self):
        self.lPointer = self.rPointer = None

if __name__ == "__main__":
    de = Deque()
    de.append(1)
    de.append(2)
    de.append(3)
    print("The initial dequeue : ")
    de.traverse()

    de.append(4)
    print ("\nThe deque after appending at right is : ")
    de.traverse()    

    # using appendleft() to insert element at right end 
    # inserts 6 at the beginning of deque
    de.appendleft(6)
    # printing modified deque
    print ("\nThe deque after appending at left is : ")
    de.traverse()

    # using pop() to delete element from right end 
    # deletes 4 from the right end of deque
    de.pop()
    # printing modified deque
    print ("\nThe deque after deleting from right is : ")
    de.traverse()

    # using popleft() to delete element from left end 
    # deletes 6 from the left end of deque
    de.popleft()
 
    # printing modified deque
    print ("\nThe deque after deleting from left is : ")
    de.traverse()

    de.empty()
    print ("\nEmpty deque")
    de.traverse()

    de.append(1)
    de.append(2)
    de.append(3)
    de.append(3)
    de.append(4)
    de.append(2)
    de.append(4)
    print("\nThe initial dequeue : ")
    de.traverse()

    # using index() to print the first occurrence of 4
    print ("\nThe number 4 first occurs at a position : ")
    print de.index(4,2,5)

    # using insert() to insert the value 3 at 5th position
    de.insert(4,3)
 
    # printing modified deque
    print ("\nThe deque after inserting 3 at 5th position is : ")
    de.traverse()

    # using count() to count the occurrences of 3
    print ("\nThe count of 3 in deque is : ")
    print (de.count(3))
 
    # using remove() to remove the first occurrence of 3
    de.remove(3)
 
    # printing modified deque
    print ("\nThe deque after deleting first occurrence of 3 is : ")
    de.traverse()

    de.empty()
    de.append(1)
    de.append(2)
    de.append(3)

    print("\nThe initial dequeue : ")
    de.traverse()

    # using extend() to add numbers to right end 
    # adds 4,5,6 to right end
    de.extend([4,5,6])
 
    # printing modified deque
    print ("\nThe deque after extending deque at end is : ")
    de.traverse()
 
    # using extendleft() to add numbers to left end 
    # adds 7,8,9 to right end
    de.extendleft([7,8,9])

    # printing modified deque
    print ("\nThe deque after extending deque at beginning is : ")
    de.traverse()

    # printing get front of deque 
    # print 7
    print "\n The front of deque"
    print de.getFront()

    # printing get rear of deque
    # print 6
    print "\n The rear of deque"
    print de.getRear()