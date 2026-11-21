class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_heap =[]
        abc = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])
        for i in range(len(nums)):
            b = heapq.heappop(min_heap)
            abc.append(b)

        # print(abc)
        return abc
        
        