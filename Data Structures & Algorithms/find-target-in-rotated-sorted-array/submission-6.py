class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m


        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l
            l = 0
        
        while l <= r:
            m = (l + r) // 2
            mVal = nums[m]
            if mVal == target:
                return m
            if mVal < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1 
            

            
        

            


        




            

