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
        if not head:
            return None
        copies = {}

        cur = head
        while cur:
            copies[cur] = Node(cur.val, None, None)
            cur = cur.next
        

        cur = head
        prevCopy = None
        while cur:
            copyCur = copies[cur]
            if prevCopy:
                prevCopy.next = copyCur
            if cur.random:
                randomCopy = copies[cur.random]
                copyCur.random = randomCopy
            cur = cur.next
            prevCopy = copyCur
        
        return copies[head]







        