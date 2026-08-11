class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif len(self.pq) == self.k:
            if val > self.pq[0]:
                heapq.heapreplace(self.pq, val)
        return self.pq[0]
