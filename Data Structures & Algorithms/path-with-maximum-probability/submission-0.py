class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [-1] * n
        dist[start_node] = 1
        for _ in range(len(edges)):
            for i in range(len(edges)):
                a, b = edges[i]
                p = succProb[i]
                if dist[a] != -1:
                    dist[b] = max(dist[b], p * dist[a])
                if dist[b] != -1:
                    dist[a] = max(dist[a], p * dist[b])

        if dist[end_node] == -1:
            return 0
        return dist[end_node]
        