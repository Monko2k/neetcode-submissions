# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        mp = {None: 0}
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                l_height = mp[node.left]
                r_height = mp[node.right]
                if abs(l_height - r_height) > 1:
                    return False
                mp[node] = max(l_height, r_height) + 1


        return True

        