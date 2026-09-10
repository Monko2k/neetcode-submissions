class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        leftMax = height[0]
        rightMax = height[-1]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]

        return res
        