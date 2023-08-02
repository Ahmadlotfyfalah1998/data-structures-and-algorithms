import re
from typing import Generic, TypeVar, Optional
K = TypeVar('K')
V = TypeVar('V')
class Hashtable(Generic[K, V]):
    def __init__(self, size: int = 100) :
        self._size: int = size
        self._buckets: list[Optional[list[tuple[K, V]]]] = [None] * size
    @property
    def size(self) :

        return self._size
    def set(self, key, value) :

        hash = self._hash(key)
        if (bucket := self._buckets[hash]) is None:
            bucket = []
        bucket.append((key, value))
        self._buckets[hash] = bucket

    def has(self, key) :

        hash = self._hash(key)
        if (bucket := self._buckets[hash]) is None:
            return False
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def _hash(self, key) :

        hash: int = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
      
      
      
      
      


def repeated_word(paragraph):
  
    '''
    this function take a (string)
    ant return a (string)
    this function use the hash table to return the first repeated word in string 
    
    
    '''
    words = re.findall(r'\w+', paragraph)
    hashtable = Hashtable()
    for word in words:
        if hashtable.has(word.lower()):
            return word
        hashtable.set(word.lower(), True)
        
        