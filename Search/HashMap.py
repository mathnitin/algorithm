#/bin/python

'''
Implement Map functionality.

  -  Map() Create a new, empty map. It returns an empty map collection.
  -  put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
  -  get(key) Given a key, return the value stored in the map or None otherwise.
  -  del Delete the key-value pair from the map using a statement of the form del map[key].
  -  len() Return the number of key-value pairs stored in the map.
  -  in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
'''

class HashMap:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        pass

    def _hashFunction(self, key):
        return key%self.size

    def _rehash(self, key):
        return (key+1)%self.size

    def put(self, key, val):
        index = self._hashFunction(key)
        if self.keys[index] == None:
            self.keys[index] = key
            self.values[index] = val
        else:
            newIndex = self._rehash(index)
            while self.keys[newIndex] != None and self.keys[newIndex] != key and newIndex != index:
                newIndex = self._rehash(newIndex)
            if self.keys[newIndex] == None:
                self.keys[newIndex] = key
                self.values[newIndex] = val
            elif self.keys[newIndex] == key:
                self.values[newIndex] = val
            elif newIndex == index:
                print 'The List is full'

    def get(self, key):
        index = self._hashFunction(key)
        if self.keys[index] == key:
            return self.values[index]
        else:
            newIndex = self._rehash(index)
            while self.keys[newIndex] != None and self.keys[newIndex] != key and newIndex != index:
                newIndex = self._rehash(newIndex)
            if self.keys[newIndex] == None:
                return None
            elif self.keys[newIndex] == key:
                return self.values[newIndex]
            elif newIndex == index:
                return None

    def delete(self, key):
        index = self._hashFunction(key)
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
        else:
            newIndex = self._rehash(index)
            while self.keys[newIndex] != key:
                newIndex = self._rehash(newIndex)
            self.keys[newIndex] = None
            self.values[newIndex] = None

    def len(self):
        return self.size

    def inOper(self, key):
        print key
        print self.size
        index = self._hashFunction(key)
        if self.keys[index] == key:
            return True
        else:
            newIndex = self._rehash(index)
            while self.keys[newIndex] != None and self.keys[newIndex] != key and newIndex != index:
                newIndex = self._rehash(newIndex)
            if self.keys[newIndex] == None:
                return False
            elif self.keys[newIndex] == key:
                return True
            elif newIndex == index:
                return False

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self.inOper(key)

    def __len__(self):
        return self.len()

if __name__ == '__main__':
    H=HashMap(8)
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print H.keys
    print H.values
    if 55 in H:
        print "Found"
        del H[55]
    if 55 in H:
        print "Found"
    else:
        print "Not found"