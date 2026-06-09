class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict1 = Counter(nums)
        abc = []
        nums1 = nums.copy()
        for i in range(len(nums)):
            if dict1[nums[i]] == 1:
                pass
            
            for j in range(dict1[nums[i]]-1):
                nums.remove(nums[i])
                nums.append('xyz')
        nums = [x for x in nums if x != 'xyz']
        return len(nums)