class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # print(10%2)
        l = 0
        # r = 2
        n = len(nums)
        if len(nums) <= 1:
            return False
        while l <=n-1:
            s1 = nums[l:]
            if sum(s1) % k == 0:
                # print(s1)
                return True
            else:
                l+=1
            # elif nums[l] > k:
            #     l+=1
            # else:
            #     r+=1
        return False
            



        # while l<r :
        #     r = l+1
        #     while r <= len(nums):
        #         s1 = sum(nums[l:r])
        #         print(s1)
        #         size = r-l #len(nums[l:r])
        #         if size >= 2 and s1 % k == 0:
        #             return True
        #         else:
        #             r+=1
        #     l+=1
        # return False
        