class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, num in enumerate(nums): 

            seek = target - num
            if seek in idx:
                return [idx.get(seek),i]
            idx[num] = i


        