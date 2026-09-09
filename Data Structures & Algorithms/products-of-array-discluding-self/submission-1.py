class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_left = []
        prods_right = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            if i == 0:
                prods_left.append(num)
            else:
                prods_left.append(prods_left[i - 1] * num)

        prods_right[-1] = (nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            prods_right[i] = (prods_right[i + 1] * num)

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(prods_right[i + 1])
            elif i == len(nums) - 1:
                res.append(prods_left[i - 1])
            else:
                left = prods_left[i - 1]
                right = prods_right[i + 1]
                res.append(left * right)
        return res
            


        