#/bin/python

'''
Implement sequential search. 

    -> Un-ordered list
    -> Ordered list
'''

class SequentialSearch:
    def __init__(self, items):
        self.items = items

    def unOrderedSearch(self, value):
        for item in self.items:
            if item == value:
                return True
        return False

    def orderedSearch(self, value):
        for item in self.items:
            if item == value:
                return True
            if item > value:
                break
        return False

if __name__ == "__main__":
    unorder = SequentialSearch([3,1,2,4,5])
    print unorder.unOrderedSearch(15)
    print unorder.unOrderedSearch(5)
    order = SequentialSearch([1,2,3,4,5])
    print order.orderedSearch(15)
    print order.orderedSearch(5)