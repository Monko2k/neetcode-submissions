class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        items = self.map[key]
        res = ""
        l = 0
        r = len(items) - 1
        while l <= r:
            m = (l + r)//2
            val, ts = items[m]
            if ts == timestamp:
                return val
            elif ts < timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
        return res


        
