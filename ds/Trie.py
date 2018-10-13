#!/bin/python

'''
https://www.geeksforgeeks.org/trie-insert-and-search/

https://www.geeksforgeeks.org/trie-delete/
'''

class TrieNode():

    def __init__(self):
        self.child = [None]*256
        self.isEnd = False

    def isAnyChild(self):
        for c in self.child:
            if c:
                return True
        return False


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, inputStr):
        node = self.root
        for char in inputStr:
            if node.child[ord(char)] is  None:
                node.child[ord(char)] = TrieNode()
            node = node.child[ord(char)]
        node.isEnd = True

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

    def delete(self, inputString, node, size, level=0):
        if not self.search(inputString):
            return False
        if level == size:
            node.isEnd = False
            return node.isAnyChild()
        else:
            node = node.child[ord(inputString[level])]
            retVal = self.delete(inputString, node, size, level+1)
            if retVal is False:
                del node.child[index]
            if node.isEnd:
                return False
            return node.isAnyChild()
            


if __name__ == "__main__":
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in tire"] 
  
    # Trie object 
    t = Trie() 


    # Construct trie 
    for key in keys: 
        t.insert(key)
  
    # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))

    print "==== After delete of 'the' ===="
    t.delete("the", t.root, len("the"))
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
