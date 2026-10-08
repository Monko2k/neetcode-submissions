class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t0 = False
        t1 = False
        t2 = False
        ta, tb, tc = target
        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue
            if a == ta:
                t0 = True
            if b == tb:
                t1 = True
            if c == tc:
                t2 = True

        return t0 and t1 and t2


        