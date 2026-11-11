class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curSum = 0
        minLen = math.inf
        while l < len(nums):
            if curSum < target:
                if r >= len(nums):
                    break
                curSum += nums[r]
                r += 1
            else:
                curLen = r - l
                minLen = min(minLen, curLen)
                curSum -= nums[l]
                l += 1





        if minLen == math.inf:
            return 0
        else:
            return minLen


        