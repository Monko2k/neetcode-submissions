# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for i, node in enumerate(lists):
            if node != None:
                val = node.val
                heapq.heappush(heap, (val, i, node))
            
        res = None
        last = None
        
        while heap:
            val, i, node = heapq.heappop(heap)
            new = ListNode(val)
            if res == None:
                res = new
            else:
                last.next = new
            last = new
            nextNode = node.next
            if nextNode:
                heapq.heappush(heap, (nextNode.val, i, nextNode))
                
        return res
        







        