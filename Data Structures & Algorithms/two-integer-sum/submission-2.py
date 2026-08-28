class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for id, num in enumerate(nums):
            dict1[num] = id
        print(dict1)
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dict1 and dict1[x] != i:
                return [i, dict1[x]]
        # for k,v in dict1.items()
        

            
        