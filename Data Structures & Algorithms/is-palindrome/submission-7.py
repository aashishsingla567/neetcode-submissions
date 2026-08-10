

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        start, end = 0, len(s) - 1
        while start < end:
            while not s[start].isalnum():
                start += 1
                if start > end:
                    return True
            while not s[end].isalnum():
                end -= 1
                if end < start:
                    return True
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1

        return True
