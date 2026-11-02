class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        reserve = defaultdict(int)
        for bill in bills:
            reserve[bill] += 1
            if bill == 5:
                continue
            if bill == 10:
                if reserve[5] == 0:
                    return False
                reserve[5] -= 1
            if bill == 20:
                if reserve[10] > 0 and reserve[5] > 0:
                    reserve[10] -= 1
                    reserve[5] -= 1
                elif reserve[5] >= 3:
                    reserve[5] -= 3
                else:
                    return False



        return True
            
        