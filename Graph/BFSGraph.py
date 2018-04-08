#!/bin/python

'''
Breadth First Traversal or BFS for a Graph
Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post). 
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing 
a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the 
starting vertex.
For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all adjacent vertices 
of it. 2 is also an adjacent vertex of 0. If we don't mark visited vertices, then 2 will be processed again and it will become a 
non-terminating process. A Breadth First Traversal of the following graph is 2, 0, 3, 1.

https://cdncontribute.geeksforgeeks.org/wp-content/uploads/bfs-5.png

Notes:
defaultdict is used as it supports key to list dictonary. This can be achieved by normal dict as well, just have to make sure that 
we do it properly as a list.
'''

from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.visitedNodes = []

    def addEdge(self, node, child):
        self.graph[node].append(child)

    def printBFS(self, startNode):
        print "\n"
        childNodes = []
        for i in startNode:
            if i in self.graph and i not in self.visitedNodes:
                print i,
                self.visitedNodes.append(i)
                for x in self.graph[i]:
                    childNodes.append(x)
        if len(childNodes) == 0:
            return
        else:
            self.printBFS(childNodes)

if __name__ == "__main__":
    tree = Graph()
    tree.addEdge(0, 1)
    tree.addEdge(0, 2)
    tree.addEdge(1, 2)
    tree.addEdge(2, 0)
    tree.addEdge(2, 3)
    tree.addEdge(3, 3)

    tree.printBFS([2])