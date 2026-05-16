class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.upper() for ch in s if ch.isalnum())
        if s[::-1] == s:
            return True
        else:
            return False

        