"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        nodes = {}
        def clone(n, nodes):

            newNeighbors = []
            newNode = Node(n.val, newNeighbors)
            nodes[n.val] = newNode
            for nb in n.neighbors:
                if nb.val in nodes:
                    newNeighbors.append(nodes[nb.val])
                    continue
                else:
                    newNeighborNode = clone(nb, nodes)
                    newNeighbors.append(newNeighborNode)
            
            return newNode
        
        return clone(node, nodes)


        