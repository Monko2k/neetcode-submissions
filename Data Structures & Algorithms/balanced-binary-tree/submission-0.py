# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal, _ = self.dfs(root)
        return bal
    
    def dfs(self, root): 
        if not root: return True, 0
        leftBal, leftHeight = self.dfs(root.left)
        rightBal, rightHeight = self.dfs(root.right)
        bal = abs(leftHeight - rightHeight) <= 1
        return leftBal and rightBal and bal, 1 + max(leftHeight, rightHeight)


