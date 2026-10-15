class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum:
            return 0

        targetRange = (2 * totalSum) + 1

        last = [None] * targetRange
        for i in range(len(nums), -1, -1):
            cur = [None] * targetRange
            for j in range(targetRange - 1, -1, -1):
                if i == len(nums):
                    if j == totalSum:
                        cur[j] = 1
                        continue
                    cur[j] = 0
                    continue

                val = nums[i]
                res = 0
                if j + val < targetRange:
                    res += last[j + val]
                if j - val >= 0:
                    res += last[j - val]
                cur[j] = res
            last = cur

        return last[target + totalSum]