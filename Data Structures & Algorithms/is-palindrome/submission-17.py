class Solution:
    def isPalindrome(self, s: str) -> bool:
        bruh = ""
        for i in s:
            if i.isalnum():
                bruh += i.upper()
        
        if bruh == bruh[::-1]:
            return True
        else:
            return False