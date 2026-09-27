class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inEdge = defaultdict(set)
        outEdge = defaultdict(set)

        visited = set()

        for a, b in prerequisites:
            inEdge[b].add(a)
            outEdge[a].add(b)

        
        queue = deque()
        visited = set()
        for course in range(numCourses):
            if course not in inEdge:
                queue.append(course)
            
        while queue:
            course = queue.pop()
            visited.add(course)
            for out in outEdge[course]:
                inEdge[out].remove(course)
                if len(inEdge[out]) == 0:
                    queue.append(out)
        
        return len(visited) == numCourses


        


        