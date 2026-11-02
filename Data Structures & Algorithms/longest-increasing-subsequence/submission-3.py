class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            l = 0
            r = len(tails) - 1
            while l <= r:
                m = l + (r - l) // 2
                t = tails[m]
                if t < num:
                    l = m + 1
                else:
                    r = m - 1

            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num
        
        return len(tails)
        