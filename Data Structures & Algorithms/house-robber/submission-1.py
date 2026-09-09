class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for num in nums:
            maxNum = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = maxNum
        
        return max(rob1, rob2)

        

                
        