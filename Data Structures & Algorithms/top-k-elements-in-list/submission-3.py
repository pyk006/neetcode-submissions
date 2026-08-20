class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1
        
        k_heap = []

        for key, value in occurences.items():
            heapq.heappush(k_heap, (value, key))

            if len(k_heap) > k:
                heapq.heappop(k_heap)
        
        return [item[1] for item in k_heap]