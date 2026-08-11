class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits[-1] += 1
        index = len(digits) - 1
        while index >= 0 and digits[index] + 1 == 10:
            print(digits)
            digits[index] = 0
            index -= 1
        if index < 0:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        return digits
