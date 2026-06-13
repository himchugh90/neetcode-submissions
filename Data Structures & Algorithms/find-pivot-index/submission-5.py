class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # print(sum(nums[:0]))
        n = len(nums)
        left_sum = 0
        pivot = 0
        total = sum(nums)
        for i in range(len(nums)):
            # left_sum = sum(nums[:i])
            
            pivot = nums[i]
            right_sum = total - left_sum - pivot
            # print(left_sum, right_sum)
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
       
        # for i in range(len(nums)-1):
        #     # left_sum = 0
        #     right_sum = sum(nums)
            
        #     right_sum -= (left_sum + nums[i+1])
        #     print(left_sum, right_sum)
        #     if left_sum == right_sum:
        #         print(i+1)
        #         return i+1
        #     left_sum +=nums[i]
        # return -1





        