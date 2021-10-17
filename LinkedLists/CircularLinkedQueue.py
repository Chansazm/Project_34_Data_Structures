class CircularQueue:
    """Queue implementation using a linked-List"""
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next) -> None:
            self._element = element
            self._next = next
            
    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        """Return True if Queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return but do not remove"""
        if self.is_empty():
            raise Exception("Queue is empty")
        head = self._tail._next
        return head._element
    def dequeue(self):
        """FIFO remove first item from queue"""
        if self.is_empty():
            raise Exception("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next # bypass the old head
            self._size -= 1
        return oldhead._element
    
    def enqueue(self,e):
        """Add an element to the back of the queue"""
        newest = self._Node(e,None)
        if self.is_empty():
            newest._next = newest
        self._tail = newest
        self._size += 1
        
    def rotate(self):
        """Rotate first element to end of queue"""
        if self._size > 0:
            self._tail = self._tail._next # old head becomes new tail
            
            