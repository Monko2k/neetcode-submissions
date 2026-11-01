class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        r = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, r - 1)
        reverse(r, len(nums) - 1)


        