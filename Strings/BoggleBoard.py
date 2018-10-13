#!/bin/python

'''
Boggle (Find all possible words in a board of characters) | Set 1
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
      boggle[][]   = {{'G','I','Z'},
                      {'U','E','K'},
                      {'Q','S','E'}};
     isWord(str): returns true if str is present in dictionary
                  else false.

Output:  Following words of dictionary are present
        GEEKS
        QUIZ
'''

class Node():
    def __init__(self):
        self.node = [None]*256
        self.isEnd = False


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curNode = self.root
        for char in word:
            if curNode.node[ord(char)] is None:
                curNode.node[ord(char)] = Node()
            curNode = curNode.node[ord(char)]
        curNode.isEnd = True


def DFS(xIndex, yIndex, boogle, visited, word, trieNode, ans):
    if xIndex < 0 or yIndex < 0 or xIndex == len(boogle) or yIndex == len(boogle[0]) or visited[xIndex][yIndex] == True or trieNode is None:
        return 
    if trieNode.node[ord(boogle[xIndex][yIndex])] is None:
        return 
    word += boogle[xIndex][yIndex]
    if trieNode.node[ord(boogle[xIndex][yIndex])].isEnd == True:
        ans.append(word)
    visited[xIndex][yIndex] = True
    DFS(xIndex-1, yIndex-1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex-1, yIndex, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex-1, yIndex+1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex, yIndex-1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex, yIndex+1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex+1, yIndex-1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex+1, yIndex, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)
    DFS(xIndex+1, yIndex+1, boogle, visited, word, trieNode.node[ord(boogle[xIndex][yIndex])], ans)


if __name__ == "__main__":
    boogle = [['G','I','Z'], ['U','E','K'], ['Q','S','E']]
    
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    trieRoot = Trie()
    for word in dictionary:
        trieRoot.insert(word)
    
    curNode = trieRoot.root
    ans = []
    for xx in range(len(boogle)):
        for yy in range(len(boogle[0])):
            #print "Main:"
            #print "xx: ",xx, "yy: ", yy 
            visited = [[False for x in range(len(boogle))] for j in range(len(boogle[0]))]
            DFS(xx, yy, boogle, visited, "", curNode, ans)
    print ans