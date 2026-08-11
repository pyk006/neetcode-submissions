class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        heap = []
        for key,value in map.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        topk = []
        for tupleval in heap:
            topk.append(tupleval[1])
        
        return topk