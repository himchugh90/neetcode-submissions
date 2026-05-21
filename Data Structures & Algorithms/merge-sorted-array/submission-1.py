class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = nums1 + nums2
        # print(nums)
        dict1 = Counter(nums1)
        x = dict1[0]
        for i in range(n):
            nums.remove(0)
        # print(nums)

        nums = sorted(nums)
        for i in range(len(nums)):
            nums1[i] = nums[i]
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        