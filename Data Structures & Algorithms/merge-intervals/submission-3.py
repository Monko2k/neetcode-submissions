class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
                continue
            last_end = res[-1][1]
            if interval[0] <= last_end:
                res[-1][1] = max(interval[1], last_end)
            else:
                res.append(interval)
        
        return res

        