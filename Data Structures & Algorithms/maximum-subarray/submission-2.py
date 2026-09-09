class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curTotal = nums[0]
        globalTotal = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curTotal = max(curTotal + num, num)
            globalTotal = max(globalTotal, curTotal)
        
        return globalTotal 
            


        