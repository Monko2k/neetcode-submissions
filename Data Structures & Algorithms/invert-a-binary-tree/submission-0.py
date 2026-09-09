# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        invertLeft = self.invertTree(root.left)
        invertRight = self.invertTree(root.right)
        root.right = invertLeft
        root.left = invertRight
        return root