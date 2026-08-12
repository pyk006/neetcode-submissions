class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        visited = set()
        best = 0
        for num in all_nums:
            if num in visited:
                continue
            else:
                start = num
                while num in all_nums:
                    visited.add(num)
                    num += 1
                
                best = max(best, num - start)
        
        return best
