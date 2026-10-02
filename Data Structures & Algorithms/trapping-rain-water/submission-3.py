class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l = 0 
        max_l = height[l]
        r = len(height) - 1
        max_r = height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                trapped += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                trapped += max_r - height[r]
        
        return trapped

        