class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        n = len(nums)
        while l<r and r<n:
            if (nums[l]%2 == 0 and nums[r]%2 == 1) or (nums[r]%2 == 0 and nums[l]%2 == 1):
                # print(nums[l], nums[r])
                l+=1
                r+=1
            else:
                return False
        return True


        