# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        group = []
        curr = head

        def reverseGroup(node):
            if node.next is None:
                return node
            reversedGroup = reverseGroup(node.next)
            reversedGroup.next = node
            node.next = None
            return node

        while curr is not None:
            group.append(curr)
            post = curr.next
            if len(group) == k:
                curr.next = None
                newLast = group[0]
                reverseGroup(group[0])
                newFirst = group[-1]
                pre.next = newFirst
                pre = newLast
                newLast.next = post
                group = []
                curr = post
            curr = post

            

        return dummy.next
        
        