import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^0-9A-Za-z]', '', s.lower());

        start = 0;
        end = len(cleaned) - 1

        while start < end:
            if cleaned[start] != cleaned[end]:
                return False;
            start += 1
            end -= 1
        return True;