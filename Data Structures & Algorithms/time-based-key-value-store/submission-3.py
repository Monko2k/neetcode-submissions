from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        items = self.map[key]
        l, r = 0, len(items) - 1
        while l <= r:
            m = (l + r) // 2
            val, ts = items[m]
            if ts == timestamp:
                return val
            elif ts < timestamp:
                l = m + 1
            else:
                r = m - 1

        return items[r][0] if r >= 0 else ""