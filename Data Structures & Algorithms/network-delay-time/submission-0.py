class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for item in times:
            u, v, w = item
            adj[u].append((v, w))

        dist = {}
        def dfs(node, generation):

            if node in dist and generation >= dist[node]: 
                return
            
            dist[node] = generation
            for neighbor, w in adj[node]:
                dfs(neighbor, generation + w)

        dfs(k, 0)


        maxDist = 0
        for i in range(1, n + 1):
            if i in dist:
                maxDist = max(maxDist, dist[i])
            else:
                return -1
                
        return maxDist