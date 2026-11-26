class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        occ = set()
        for right in range(0, len(nums)):
            if abs(right - left) > k:
                occ.remove(nums[left])
                left += 1
            if nums[right] in occ:
                return True
            occ.add(nums[right])
            

        return False