class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        l = 0
        r = 1
        n = len(nums)
        s = 0 # nums[0]
        min_len = float('inf')
        for r in range(n):
            s+=nums[r]
            while s>= target:
                min_len = min(min_len, r-l+1)
                s-=nums[l]
                l+=1
        return 0 if min_len == float('inf') else min_len
