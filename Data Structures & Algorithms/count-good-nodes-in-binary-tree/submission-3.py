# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0 

        def isGood(node, maxVal):

            good = 0
            if node.val >= maxVal:
                good += 1
            
            newMax = max(maxVal, node.val)
            if node.left:
                good += isGood(node.left, newMax)
            if node.right:
                good += isGood(node.right, newMax)
            return good
        
        return isGood(root, -math.inf)
        