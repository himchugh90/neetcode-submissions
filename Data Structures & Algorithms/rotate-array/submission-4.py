class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # s = [1,2,3,4,5,6,7,8]
        # print(s[-2])
        # print(s[:4])
        # print(s[-4:])
        # l = 0
        n = len(nums)
        # r = k
        # while l< n:
        #     left = nums[-k:]
        #     right = nums[k:]
        #     s = left+right
        # return s
        if k > n:
            k = k%n
        nums1 = nums.copy()
        for i in range(k):
            nums[i] = nums[n-k+i]
        for i in range(n-k):
            nums[k+i] = nums1[i]
        # print(nums1)
        #for i in range(len(nums)):
        #    nums[i] = nums1[i]
        
        
        # nums[-k:] + nums[:k]
        
        """
        Do not return anything, modify nums in-place instead.
        """
        