class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min_heap = []
        self.k = k
        self.min_heap = nums
        if self.min_heap:
            heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
       


    def add(self, val: int) -> int:
        # if self.min_heap:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        
      
      