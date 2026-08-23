class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        best = float('infinity')
        count = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                count += 1
            
            if (right - left + 1) == k:
                best = min(count, best)
                if blocks[left] == "W":
                    count -= 1
                left += 1
        
        return best
