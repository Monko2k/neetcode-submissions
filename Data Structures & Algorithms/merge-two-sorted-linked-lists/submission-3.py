# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        head = None
        if h1 and h2:
            if h1.val < h2.val:
                head = h1
                h1 = h1.next
            else:
                head = h2
                h2 = h2.next
        elif h1:
            return h1
        else: 
            return h2

        last = head
        while h1 and h2:
            if h1.val < h2.val:
                last.next = h1
                h1 = h1.next
            else:
                last.next = h2
                h2 = h2.next
            last = last.next
            last.next = None
        if h1:
            last.next = h1
        if h2:
            last.next = h2


        return head
        