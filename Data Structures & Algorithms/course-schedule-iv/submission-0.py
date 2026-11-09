class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        unlocks = defaultdict(set)
        for a, b in prerequisites:
            unlocks[a].add(b)
        
        dived = set()
        
        def dfs(a):
            if a in dived:
                return unlocks[a]
            dived.add(a)
            reachable = set()
            for b in unlocks[a]:
                reachable.update(dfs(b))
            unlocks[a].update(reachable)
            return unlocks[a]
        

        res = []
        for a, b in queries:
            dfs(a)
            res.append(b in unlocks[a])

        return res

            


        

        