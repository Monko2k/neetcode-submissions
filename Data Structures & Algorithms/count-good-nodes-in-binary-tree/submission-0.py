# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def rec(node, greatest):
            if node == None:
                return 0 
            if node.val >= greatest:
                left = rec(node.left, node.val)
                right = rec(node.right, node.val)
                return left + right + 1
            else:
                left = rec(node.left, greatest)
                right = rec(node.right, greatest)
                return left + right


        return rec(root, -math.inf)
    
        