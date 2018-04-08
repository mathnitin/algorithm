#!/bin/python

'''
Given a Complete Binary tree, print the level order traversal in sorted order.

Input:
The first line takes an integer n denoting the size of array i.e number of nodes followed by n-space separated integers 
denoting the nodes of the tree in level order fashion.

Output:
The output is the level order sorted tree.
Note:  For every level, we only print distinct elements.

Constraints:
1<=T<=100
1<=n<=10^5

Example:
Input:
7
7 6 5 4 3 2 1
Output:
7
5 6
1 2 3 4

Input:
6
5 6 4 9 2 1 
Output:
5
4 6
1 2 9

Explanation:
Tree looks like this   

            7
          /    \
        6       5
       / \     / \
      4  3    2   1
Sorted order:
7
5 6
1 2 3 4
'''
class Queue():
    def __init__(self):
        self.items = []
        self.isEmpty = True

    def enqueue(self, data):
        self.items.append(data)
        self.isEmpty = False

    def dequeue(self):
        if len(self.items) == 0:
            self.isEmpty = True
            return
        elem = self.items[0]
        del self.items[0]
        return elem
    

def findChild(parentQueue, tree):
    childQueue = Queue()
    while not parentQueue.isEmpty:
        node = parentQueue.dequeue()
        if node is None:
            return childQueue
        index = node[1]
        if (2*index+1) < len(tree):
            childQueue.enqueue((tree[2*index+1], 2*index+1))
        if (2*index+2) < len(tree):
            childQueue.enqueue((tree[2*index+2], 2*index+2))
    return childQueue

if __name__ == "__main__":
    tree = [7, 6, 5, 4, 3, 2, 1]
    array = []
    parentQueue = Queue()
    if parentQueue.isEmpty:
        parentQueue.enqueue((tree[0], 0))
        print tree[0]
    while True:
        childQueue = findChild(parentQueue, tree)
        if childQueue.isEmpty:
            break
        while not parentQueue.isEmpty:
            parentQueue.dequeue()
        while not childQueue.isEmpty:
            elem = childQueue.dequeue()
            if elem is not None and elem[0] not in array:
                array.append(elem[0])
            parentQueue.enqueue(elem)
        for i in sorted(array):
            print i,
        print ""
        array = []
