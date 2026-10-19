class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_1 <= stone_2:
                stone_1 = stone_1 - stone_2
                heapq.heappush(stones, stone_1)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]