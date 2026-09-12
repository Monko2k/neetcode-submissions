# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        c1 = l1
        c2 = l2
        res = None
        prev = None
        while c1 or c2:
            val1 = 0
            val2 = 0
            if c1 != None:
                val1 = c1.val
                c1 = c1.next
            if c2 != None:
                val2 = c2.val
                c2 = c2.next

            cSum = carry + val1 + val2
            val = cSum % 10
            carry = cSum // 10
            node = ListNode(val)
            if res == None:
                res = node
            if prev:
                prev.next = node
            prev = node
        if carry > 0:
            prev.next = ListNode(1)
        return res




            

        