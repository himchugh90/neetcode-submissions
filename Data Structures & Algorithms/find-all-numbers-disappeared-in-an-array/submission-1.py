class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        abc = []
        for i in range(1,n+1):
            abc.append(i)
        print(abc)
        d = [x for x in abc if x not in nums]
        return d

        # min_x = min(nums)
        # max_x = max(nums)
        # # nums = sorted(nums)
        # if len(set(nums)) == 1:
        #     return [nums[0]+1]
        # abc = []
        # for i in range(min_x, max_x+1):
        #     abc.append(i)
        # d = [x for x in abc if x not in nums]
        # return d

        