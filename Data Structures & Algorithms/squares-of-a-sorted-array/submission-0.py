class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        abc = []
        for i in range(len(nums)):
            a = nums[i]**2
            abc.append(a)
        return sorted(abc)

        