class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        last = None
        nums.sort()
        for num in nums:
            if num == last:
                return True
            else:
                last = num
        return False
