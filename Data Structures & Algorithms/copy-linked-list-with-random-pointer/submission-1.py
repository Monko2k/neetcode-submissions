"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cur = head
        while cur:
            copy = Node(cur.val)
            copy.random = cur.random
            cur.random = copy
            cur = cur.next
        
        newHead = head.random
        cur = head
        while cur:
            copy = cur.random
            if copy.random:
                copy.random = copy.random.random
            if cur.next:
                copy.next = cur.next.random
            cur = cur.next
        
        return newHead
            
        