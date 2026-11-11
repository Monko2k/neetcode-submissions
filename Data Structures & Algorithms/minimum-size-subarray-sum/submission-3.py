class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = []
        for i in range(len(nums) + 1):
            if i == 0:
                prefix.append(0)
            else:
                prefixSum = nums[i - 1] + prefix[i - 1]
                prefix.append(prefixSum)
        minLen = math.inf
        for i in range(len(nums)):
            l = i
            r = len(nums)
            while l <= r:
                m = l + (r - l) // 2
                total = prefix[m] - prefix[i]
                if total >= target:
                    minLen = min(minLen, m - i)
                    r = m - 1
                else:
                    l = m + 1

        if minLen == math.inf:
            return 0
        return minLen

        
        