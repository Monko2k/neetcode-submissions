# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.next is None:
                break
            nextNode = curr.next
            gcd = math.gcd(curr.val, nextNode.val)
            newNode = ListNode(gcd, nextNode)
            curr.next = newNode
            newNode.next = nextNode
            curr = nextNode

        return head
        