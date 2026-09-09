class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if len(res) == 0:
                res.append([start, end])
                continue
            prev_start, prev_end = res[-1]
            if start <= prev_end:
                res[-1][1] = max(end, prev_end)
            else:
                res.append([start, end])
        return res 
            
            


        