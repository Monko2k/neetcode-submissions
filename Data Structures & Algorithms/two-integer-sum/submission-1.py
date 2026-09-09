class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCache = {}
        for i, num in enumerate(nums):
            seek = target - num
            if seek in numCache:
                return [numCache[seek], i]
            numCache[num] = i
        

        