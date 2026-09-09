# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        
        def rec(node, lowerBound, upperBound):
            if node == None:
                return True
                
            if node.val <= lowerBound or node.val >= upperBound:
                return False
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False
            left = rec(node.left, lowerBound, node.val)
            right = rec(node.right, node.val, upperBound)
            return left and right

        return rec(root, -math.inf, math.inf)
