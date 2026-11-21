class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = Counter(nums)
        # print(f)
        min_heap = []
        a = list(f.values())
        for i in range(len(a)):
            heapq.heappush(min_heap, -a[i])
        # print(min_heap)
        # print(heapq.heappop(min_heap))

        b = [heapq.heappop(min_heap) for _ in range(k)]
        # print(b)
        abc = []
        for k,v in f.items():
            if -f[k] in b:
                abc.append(k)
        return abc