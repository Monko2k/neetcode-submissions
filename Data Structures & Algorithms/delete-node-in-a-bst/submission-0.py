# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(node, val, parent):
            if node is None: 
                return (None, None)
            if node.val == val:
                return (node, parent)
            elif node.val > val:
                return find(node.left, val, node)
            else:
                return find(node.right, val, node)
            
        def insert(node, newNode):
            if node is None:
                return newNode
            if newNode is None:
                return node
            
            if newNode.val > node.val:
                if node.right:
                    return insert(node.right, newNode)
                else:
                    node.right = newNode
                    return node
            else:
                if node.left:
                    return insert(node.left, newNode)
                else:
                    node.left = newNode
                    return node
        
        node, parent = find(root, key, None)
        if node is None:
            return root
        
        newTree = None
        if node.right:
            newTree = node.right
            insert(newTree, node.left)
        else:
            newTree = node.left

        if parent is None:
            return newTree
        else:
            if node.val < parent.val:
                parent.left = None
            else:
                parent.right = None
            insert(parent, newTree)
            return root

            

        