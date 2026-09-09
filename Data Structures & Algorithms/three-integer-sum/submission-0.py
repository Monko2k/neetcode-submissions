class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (nums[l - 1] == nums[l] and l < r):
                        l += 1
                elif threeSum < 0:
                    l += 1
                else: 
                    r -= 1
        return res


        
        
        