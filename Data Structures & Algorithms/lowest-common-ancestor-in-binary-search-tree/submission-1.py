# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = set()
        ancestors.add(root)
        cur = root
        while cur != p:
            if cur.val < p.val:
                cur = cur.right
            else:
                cur = cur.left
            ancestors.add(cur)
        ancestors.add(cur)

        if q in ancestors:
            return q
        
        lca = root
        cur = root
        while cur != q:
            print(cur.val)
            if cur in ancestors:
                lca = cur
            if cur.val < q.val:
                cur = cur.right
            else:
                cur = cur.left
        
        return lca
            


        