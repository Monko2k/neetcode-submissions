class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requires = defaultdict(set)
        satisfies = defaultdict(set)

        for a, b in prerequisites:
            satisfies[b].add(a)
            requires[a].add(b)
            

        q = deque()
        courses = []
        def sat(a):
            courses.append(a)
            for b in satisfies[a]:
                requires[b].remove(a)
                if len(requires[b]) == 0:
                    sat(b)
        
        for i in range(numCourses):
            if i not in requires:
                sat(i)

        if len(courses) == numCourses:
            return courses

        return []
    
        



        

        