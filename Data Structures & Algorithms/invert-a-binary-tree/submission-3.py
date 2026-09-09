# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            item = queue.popleft()
            dummy = item.right
            item.right = item.left
            item.left = dummy
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        
        return root

        