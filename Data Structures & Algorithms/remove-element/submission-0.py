class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dict1 = Counter(nums)
        k = 0
        for i in range(dict1[val]):
            nums.remove(val)
            nums.append('xyz')
            k+=1
        print(nums)
        
        return len(nums)-k

        # # nums1 = nums
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         k+=1
        # return k
        # # print(k)

