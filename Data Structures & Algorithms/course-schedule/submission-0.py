class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requires = defaultdict(set)
        satisfies = defaultdict(set)

        for a, b in prerequisites:
            satisfies[a].add(b)
            requires[b].add(a)
            
        def sat(a):
            for b in satisfies[a]:
                requires[b].remove(a)
                if len(requires[b]) == 0:
                    sat(b)
        
        for i in range(numCourses):
            if i not in requires:
                sat(i)
        
        for item in requires.values():
            if len(item) > 0:
                return False
        
        return True
        



        