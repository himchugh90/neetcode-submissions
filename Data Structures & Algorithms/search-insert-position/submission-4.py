class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
    
        while l<=r:
            m = (l+r)//2
            print(m)
            if target > nums[r]:
                return r+1
            elif target < nums[l]:
                return l
            
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
                # print(l)
            else: #target <= nums[m]:
                r = m
        return l

        