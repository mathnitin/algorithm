# Implementation of Binary Tree.

### Binary Tree: 
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can 
have only 2 children, we typically name them the left and right child.

Facts:
1) The maximum number of nodes at level ‘l’ of a binary tree is 2^(l-1)
2) Maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1
3) In a Binary Tree with N nodes, minimum possible height or minimum number of levels is  ⌈ Log(N+1) ⌉ 
4) A Binary Tree with L leaves has at least   ⌈ Log2L ⌉ + 1   levels
5) In Binary tree, number of leaf nodes is always one more than nodes with two children.

### Full Binary Tree 
A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree. We can 
also say a full binary tree is a binary tree in which all nodes except leaves have two children.

               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40

             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50

               18
            /     \  
          40       30  
                   /  \
                 100   40

### Complete Binary Tree
A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level 
and the last level has all keys as left as possible.

Following are examples of Complete Binary Trees

               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9 
Practical example of Complete Binary Tree is Binary Heap.

### Perfect Binary Tree 
A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at 
same level. Following are examples of Perfect Binaryr Trees.

               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


               18
           /       \  
         15         30  

### Balanced Binary Tree
A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. For Example, AVL tree maintain O(Log n) 
height by making sure that the difference between heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) 
height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. 
Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.

### A degenerate (or pathological) tree 
A Tree where every internal node has one child. Such trees are performance-wise same as linked list.

      10
      /
    20
     \
     30
      \
      40     

### Tree Traversals (Inorder, Preorder and Postorder)

Following are the generally used ways for traversing trees.

            1
           /  \   
          2    3    
        /  \       
       4    5   

#### Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

#### Breadth First or Level Order Traversal 
1 2 3 4 5