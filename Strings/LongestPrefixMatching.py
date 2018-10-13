#!/bin/python
'''
https://www.geeksforgeeks.org/longest-prefix-matching-a-trie-based-solution-in-java/

Given a dictionary of words and an input string, find the longest prefix of the string which is also a word in dictionary.
Examples:

Let the dictionary contains the following words:
{are, area, base, cat, cater, children, basement}

Below are some input/output examples:
--------------------------------------
Input String            Output
--------------------------------------
caterer                 cater
basemexy                base
child                   < Empty >
'''

class TrieNode():
    def __init__(self):
        self.child = [None]*256
        self.isEnd = False
    

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, inputStr):
        node = self.root
        for ch in inputStr:
            if node.child[ord(ch)] is None:
                node.child[ord(ch)] = TrieNode()
            node=node.child[ord(ch)]
        node.isEnd = True

    def bestMatch(self, inputString):
        matchStr = None
        node = self.root
        size = len(inputString)
        for index in range(size):
            ch = inputString[index]
            if node.child[ord(ch)] is None:
                return matchStr
            node = node.child[ord(ch)]
            if node.isEnd:
                matchStr = inputString[:index+1]
        return matchStr

    def search(self, inputStr):
        node = self.root
        size = len(inputStr)
        for index in range(size):
            char = inputStr[index]
            if node.child[ord(char)] is None:
                return False
            node = node.child[ord(char)]
        if node is None:
            return False
        return node.isEnd


if __name__ == "__main__":
    words = ["are", "area", "base", "cat", "cater", "children", "basement"]
    t = Trie()
    for word in words:
        t.insert(word)
    
    print "Best Match caterer", t.bestMatch("caterer")
    print "Best Match basemexy", t.bestMatch("basemexy")
    print "Best Match child", t.bestMatch("child")
    print "Best Match are", t.bestMatch("are")
    print "Best Match ared", t.bestMatch("ared")
    print "Best Match area", t.bestMatch("area")
    print "Best Match areaed", t.bestMatch("areaed")