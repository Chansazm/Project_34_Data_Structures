class PriorityQueueBaseclass:
    """A priority abstract base class for a priority queue"""
    class _Item:
        """Lightweight composite storing items"""
        __slots__ = '_key','_value'
        
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def It(self,other):
            return self._key < other._key
        
        def is_empty(self):
            return len(self) == 0
        
        
        