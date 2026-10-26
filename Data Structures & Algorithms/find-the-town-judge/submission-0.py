class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inMap = defaultdict(list)
        out = set()
        people = set()
        for a, b in trust:
            inMap[b].append(a)
            out.add(a)
            people.add(a)
            people.add(b)
        
        for key, val in inMap.items():
            if len(val) == len(people) - 1 and key not in out:
                return key
        return -1
        


        