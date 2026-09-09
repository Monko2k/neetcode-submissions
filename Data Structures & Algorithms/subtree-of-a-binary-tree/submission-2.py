# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        mainRep = self.dfs(root)
        subRep = self.dfs(subRoot)
        return subRep in mainRep
        
        
    def dfs(self, root):
        if not root:
            return "#"
        return "$" + str(root.val) + self.dfs(root.left) + self.dfs(root.right)


        