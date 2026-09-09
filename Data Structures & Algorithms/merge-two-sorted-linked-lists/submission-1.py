# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2 
        if p1 == None: return p2
        if p2 == None: return p1
    
        head = list1
        if list2.val < list1.val:
            head = list2
            p2 = list2.next
        else:
            p1 = list1.next
        prev = head
        while p1 or p2:
            if p1 == None:
                prev.next = p2
                return head
            elif p2 == None:
                prev.next = p1
                return head
            elif p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
                prev = prev.next
            elif p1.val > p2.val:
                prev.next = p2
                p2 = p2.next
                prev = prev.next
    
        return head