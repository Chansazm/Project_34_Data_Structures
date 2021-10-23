#An implementation of a map using a Python list as an unsorted table.
class Map:
    class _Item:
        __slots = '_key','_value'
        
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def __eq__(self,other):
            return self._key == other._key
        
        def __noteq__(self,other):
            return not (self._key == other._key)
        
        def __Lt__(self,other):
            return self._key < other._key

class UnsortedTableMap(Map):
    
    def __init__(self):
        self._table = []
        
    def __getitem(self,k):
        for item in self._table:
            if k == self._key:
                return item._value
        raise KeyError('key error' + repr(k))
    
    def __setitem(self,k,v):
        #Assign value v to key k, overwriting existing value if present.”””
        for item in self._table:
            if k == self._key:
                self._value = v
                return
        self._table.append(self._Item(k,v))
        
    def __delitem__(self,k):
        for j in range(self._table):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key error' + repr(k))
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key
        
    
    
                
                
    
        
        
        