# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        rep = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                rep.append("*")
            else:
                rep.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(rep)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        parts = data.split(',')
        queue = deque(parts)
        root = TreeNode(queue.popleft())
        level = [root]
        nextLevel = []
        while queue:
            for i in range(2 * len(level)):
                nodeVal = queue.popleft()
                if nodeVal == "*":
                    continue
                newNode = TreeNode(int(nodeVal))
                # 0, 1 -> 0 | 2, 3 -> 1
                levelIndex = i // 2
                if i % 2:
                    level[levelIndex].right = newNode
                else:
                    level[levelIndex].left = newNode
                nextLevel.append(newNode)
            level = nextLevel
            nextLevel = []
        return root



