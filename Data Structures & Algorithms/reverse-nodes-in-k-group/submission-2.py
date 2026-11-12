# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while True:
            kth = pre
            for _ in range(k):
                if kth.next is None:
                    return dummy.next
                kth = kth.next
            post = kth.next
            prev = post
            curr = pre.next
            while curr is not post:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            oldFirst = pre.next
            pre.next = kth
            pre = oldFirst
            
            
            
            

        