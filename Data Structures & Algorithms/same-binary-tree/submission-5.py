# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        leftq = deque([p])
        rightq = deque([q])

        while leftq and rightq:
            left = leftq.pop()
            right = rightq.pop()
            if left and not right: return False
            if right and not left: return False
            if left:
                leftq.append(left.left)
                leftq.append(left.right)
            if right:
                rightq.append(right.left)
                rightq.append(right.right)
            if not left and not right: continue
            if left.val != right.val:
                return False


        if leftq or rightq: return False
        return True

        
        