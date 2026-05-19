class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1
        max_length = 1
        if len(nums) == 0:
            return 0
        # print(sorted(nums))
        nums = sorted(list(set(nums)))
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                print(nums[i])
                max_len+=1
                max_length=max(max_len, max_length)
            else:
                i+=1
                max_len = 1
        # print(max_len)
        return max_length



        



















