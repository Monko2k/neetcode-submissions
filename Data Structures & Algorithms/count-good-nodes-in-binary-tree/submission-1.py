# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def isGood(prevMax, node):
            good = 0
            if node is None:
                return good
            if prevMax <= node.val:
                good = 1
            
            newMax = max(prevMax, node.val)
            
            good += isGood(newMax, node.left)
            good += isGood(newMax, node.right)
            return good
        
        return isGood(-math.inf, root)
        