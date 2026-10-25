class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        candidate = None
        for num in nums:
            if votes == 0:
                candidate = num
            if num == candidate:
                votes += 1
            else:
                votes -= 1
            
        return candidate
        
        