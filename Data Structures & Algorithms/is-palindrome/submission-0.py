class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char
        new_s = new_s.lower()
        
        if len(new_s) == 0 or len(new_s) == 1:
            return True
 
        start = 0
        end = len(new_s) - 1

        for i in range(len(new_s)):
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        
        return True