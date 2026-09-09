class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem_1 = [-1] * (len(nums) - 1)
        mem_2 = [-1] * (len(nums) - 1)
        def dfs(i, mem, sub_nums):
            if i >= len(mem):
                return 0 
            if mem[i] != -1:
                return mem[i]
            
            rob = sub_nums[i] + dfs(i + 2, mem, sub_nums)
            skip = dfs(i + 1, mem, sub_nums)
            val = max(rob, skip)
            mem[i] = val
            return val

        dfs(0, mem_1, nums[1:])
        dfs(0, mem_2, nums[:-1])
        max_mem1 = max(mem_1)
        max_mem2 = max(mem_2)
        
        return max(max_mem1, max_mem2)


        