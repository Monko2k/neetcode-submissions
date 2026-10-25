class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, num in enumerate(nums):
            if num == val:
                count += 1
            else:
                nums[i - count] = num
        
        return len(nums) - count
        