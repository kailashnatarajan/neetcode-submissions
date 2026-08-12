class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        stop = len(s)-1
        while start <= stop:
            if not s[start].isalpha():
                start += 1
            elif not s[stop].isalpha():
                stop -= 1
            elif s[start].lower() == s[stop].lower():
                start += 1
                stop -= 1
            else:
                return False
        return True
