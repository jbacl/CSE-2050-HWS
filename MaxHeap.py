class Entry:
   def __init__(self, priority, item):
       """Initializes an item and its priority"""
       self.priority = priority
       self.item = item
 
   def __gt__(self, other):
       """Checks if the self priority is greater than the other priority"""
       len1 = len(self.priority)
       len2 = len(other.priority)
       minlen = min(len1, len2)
       i = 0
 
       while i < minlen:
           if self.priority[i] == other.priority[i]:
               i += 1
               continue
 
           return self.priority[i] > other.priority[i]
      
       return i < len1
 
   def __eq__(self, other):
       """Checks if the self priority is equal to the other priority"""
       if self.priority == None:
           self.priority = 0
      
       if other.priority == None:
           other.priority = 0
 
       return self.priority == other.priority and self.item == other.item
 
   # repr is provided for you
   def __repr__(self):
       """Returns string representation of an Entry """
       return f"Entry(priority={self.priority}, item={self.item})"
 
 
# TODO: _heapify_up, _heapify_down, put, remove_max
class MaxHeap:
   # init is provided for you, but you should modify the default `heapify_direction` value
   def __init__(self, items=None, heapify_direction="down"):
       """Initializes a new MaxHeap with optional collection of items"""
       self._L = []
 
       # if a collection of items is passed in, heapify it
       if items is not None:
           self._L = list(items)
           if heapify_direction == 'up': self._heapify_up()
 
           elif heapify_direction == 'down': self._heapify_down()
 
           else: raise RuntimeError("Replace `heapify_direction` default with 'up' or 'down' instead of `None`")
 
   def _heapify_up(self):
       """Heapifies self._L in-place using only upheap"""
       n = len(self._L)
       for i in range(n):
           self._upheap(i)
 
   def _heapify_down(self):
       """Heapifies self._L in-place using only downheap"""
       s_i = 0
       n = len(self._L)
       while s_i > 0 and (2*s_i+1) is None:
           s_i -= 1
       for i in (range(s_i, -1, -1)):
           self._downheap(i)
 
   def put(self, entry):
       """Adds an entry to the list of priorities"""
       self._L.append(entry) # adds an entry
       self._upheap(len(self._L)-1) # upheaps the entry
 
   def remove_max(self):
       """Removes and returns the max"""
       if self._L == []:
           raise RuntimeError # raises error if list is empty
 
       max = self._L[0].item
       self._L[0] = self._L[-1] # swaps first item with last
       self._L.pop() # pops the max item
       self._downheap(0)
       return max
 
   # len is number of items in PQ
   def __len__(self):
       """Number of items in PQ"""
       return len(self._L)
 
   #TODO: Add any private helper functions (e.g. _left, _right, _upheap, ...) below
 
   def _parent(self, i):
       return (i - 1) // 2
  
   def _children(self, index):
       left = 2 * index + 1
       right = 2 * index + 2
       return range(left, min(len(self._L), right + 1))
  
   def _swap(self, a ,b):
       """Helper function that swaps values"""
       self._L[a], self._L[b] = self._L[b], self._L[a]
  
   def _downheap(self, i):
       """Swaps the value with child"""
       children = self._children(i)
       if children:
           child = min(children, key = lambda x: self._L[x])
           if self._L[child] > self._L[i]:
               self._swap(i, child)
               self._downheap(child)
  
   def _upheap(self, i):
       """Swaps the value with parent"""
       parent = self._parent(i)
       if i > 0 and self._L[i] > self._L[parent]:
           self._swap(i, parent)
           self._upheap(parent)
