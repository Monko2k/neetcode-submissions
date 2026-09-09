class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h_l = heights[l]
            h_r = heights[r]
            w = r - l
            vol = min(h_l, h_r) * w
            maxArea = max(maxArea, vol)
            if h_l < h_r:
                l += 1
            else:
                r -= 1 
        return maxArea


        