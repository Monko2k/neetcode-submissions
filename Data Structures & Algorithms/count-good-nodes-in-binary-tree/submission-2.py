# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        queue = deque()
        queue.append((root, -math.inf))
        while queue:
            node, prevMax = queue.popleft()
            if node.val >= prevMax:
                good += 1
            
            newMax = max(prevMax, node.val)
            
            if node.left is not None:
                queue.append((node.left, newMax))
            if node.right is not None:
                queue.append((node.right, newMax))

        return good
        
