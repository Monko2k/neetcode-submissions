class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        totalNonZero = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
            else:
                totalNonZero *= num

        res = []
        for num in nums:
            if num == 0 and zeroCount == 1:
                res.append(totalNonZero)
            else:
                if zeroCount > 0:
                    res.append(0)
                else:
                    res.append(totalNonZero//num)

        return res
        