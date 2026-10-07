class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        leftMost = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [len(heights)] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0

        for i in range(len(heights)):
            left = leftMost[i]
            right = rightMost[i]
            area = heights[i] * (right - left - 1)
            maxArea = max(area, maxArea)
        
        return maxArea


            
            
        