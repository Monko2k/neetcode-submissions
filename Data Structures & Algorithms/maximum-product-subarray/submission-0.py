class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        globalMax = maxProd
        for i in range(1, len(nums)):
            num = nums[i]
            newMax = maxProd * num
            newMin = minProd * num

            maxProd = max(newMax, newMin, num)
            minProd = min(newMax, newMin, num)
            globalMax = max(maxProd, globalMax)
        return globalMax




        