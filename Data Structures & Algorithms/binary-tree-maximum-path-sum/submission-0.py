# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        maxPath = root.val

        def dfs(node):
            nonlocal maxPath

            if node is None:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            through = leftMax + node.val + rightMax
            maxPath = max(through, maxPath)
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return maxPath
            