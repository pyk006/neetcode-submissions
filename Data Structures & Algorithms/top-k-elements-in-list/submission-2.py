class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}

        for num in nums:
            if num not in occur:
                occur[num] = 1
            else:
                occur[num] += 1
        
        k_heap = []
        for key, value in occur.items():
            heapq.heappush(k_heap, (value, key))
        
            if len(k_heap) > k:
                heapq.heappop(k_heap)
        
        return [value[1] for value in k_heap]