# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while True:
            kth = pre
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            post = kth.next
            prev = post
            curr = pre.next
            while curr is not post:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            oldFirst = pre.next
            pre.next = kth
            pre = oldFirst
        