class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        while cur < len(nums) - 1:
            maxJump = 0
            maxIndex = cur
            if nums[cur] == 0:
                return False
            if cur + nums[cur] >= (len(nums) - 1):
                return True
            
            for i in range(cur + 1, cur + nums[cur] + 1):
                jumpDist = nums[i] + i
                if jumpDist >= maxJump:
                    maxIndex = i
                    maxJump = jumpDist
            cur = maxIndex

        return True
        