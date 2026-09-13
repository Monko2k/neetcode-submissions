class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first = None
        self.last = None
        self.size = 0
    
    def _remove(self, node):
        if self.first == node and self.last == node:
            self.first = None
            self.last = None
        
        elif self.first == node:
            self.first = self.first.next
            self.first.prev = None
        elif self.last == node:
            self.last = self.last.prev
            self.last.next = None
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _add(self, node):
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            node.next = None
            self.last = node

    def get(self, key: int) -> int:
        if key in self.cache:
            val, node = self.cache[key]
            self._remove(node)
            self._add(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key][1]
            self.cache[key] = (value, node)
            self._remove(node)
            self._add(node)
        else:
            if self.size >= self.capacity:
                # evict
                evictNode = self.first
                self.cache.pop(evictNode.val)
                self._remove(evictNode)
                self.size -= 1
            
            self.size += 1
            new = ListNode(key)
            self._add(new)
            self.cache[key] = (value, new)

        
        

        
