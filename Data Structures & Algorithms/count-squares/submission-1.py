class CountSquares:

    def __init__(self):
        self.xIndex = defaultdict(set)
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point

        self.xIndex[x].add((x, y))
        self.pointCount[(x, y)] += 1
        
    def checkPoints(self, points):
        ways = 1
        for point in points:
            if point not in self.pointCount:
                return 0
            x, y = point
            ways *= self.pointCount[(x, y)]
        return ways

    def count(self, point: List[int]) -> int:
        x, y = point
        totalWays = 0
        for dx, dy in self.xIndex[x]:
            if y == dy:
                continue
            sidelen = abs(dy - y)
            points = [(dx, dy), (x + sidelen, dy), (x + sidelen, y)]
            totalWays += self.checkPoints(points)
            points = [(dx, dy), (x - sidelen, dy), (x - sidelen, y)]
            totalWays += self.checkPoints(points)

        return totalWays


        
