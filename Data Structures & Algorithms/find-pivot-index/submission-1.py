class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # a = [2,3,4, 5,6]
        # print(sum(a))

        # print(sum(a[2:]))
        # print(sum(a[:2]))

        
        for i in range(len(nums)):
            if sum(nums[i+1:]) == sum(nums[:i]):
                return i
        return -1



        