# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        iters = len(stack)//2
        for i in range(iters):
            temp = curr.next
            end = stack.pop()
            curr.next = end
            end.next = temp
            curr = temp

        curr.next = None




        