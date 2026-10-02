class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l = 0 
        max_l = height[l]
        r = len(height) - 1
        max_r = height[r]
        while l < r:
            l_height = height[l]
            r_height = height[r]
            if l_height < r_height:
                l += 1
                max_l = max(max_l, height[l])
                new = max(0, max_l - height[l])
                trapped += new
            else:
                r -= 1
                max_r = max(max_r, height[r])
                new = max(0, max_r - height[r])
                trapped += new
        
        return trapped

        