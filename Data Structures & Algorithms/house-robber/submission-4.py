class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0
        for num in nums:
            rob1 = num + house1
            rob2 = house2
            house1 = house2
            house2 = max(rob1, rob2)
        
        return house2
        