'''
Convert a given tree to its Sum Tree
Given a Binary Tree where each node has positive and negative values. Convert this to a tree where each node contains the sum of the 
left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

For example, the following tree

                  10
               /      \
             -2        6
           /   \      /  \ 
          8     -4    7    5
should be changed to

                 20(4-2+12+6)
               /      \
       4(8-4)      12(7+5)
           /   \      /  \ 
     0      0    0    0
'''

from ds.Queue import Queue

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def __traverse(self, queue):
        newQueue = Queue()
        while not queue.isEmpty:
            elem = queue.dequeue()
            if elem is not None:
                print elem.data,
                newQueue.enqueue(elem.left)
                newQueue.enqueue(elem.right)
        if not newQueue.isEmpty:
            self.__traverse(newQueue)

    def traverse(self):
        if self.root is None:
            return
        print self.root.data,
        queue = Queue()
        queue.enqueue(self.root.left)
        queue.enqueue(self.root.right)
        self.__traverse(queue)

def SumTree(node):
    if node.left is None and node.right is None:
        curVal = node.data
        node.data = 0
        return curVal
    else:
        curVal = node.data
        node.data = SumTree(node.left) + SumTree(node.right)
        return curVal+node.data

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(-2)
    n3 = Node(6)
    n4 = Node(8)
    n5 = Node(-4)
    n6 = Node(7)
    n7 = Node(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    tree = Tree(n1)
    tree.traverse()
    print "\nSum Tree"
    SumTree(tree.root)
    tree.traverse()

