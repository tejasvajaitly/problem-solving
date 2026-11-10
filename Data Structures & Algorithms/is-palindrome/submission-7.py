class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower()

        while left < right:
            while left < right and  not self.alphaNum(s[left]):
                left = left + 1
            while left < right and not self.alphaNum(s[right]):
                right = right - 1
            print(s[left], s[right])
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        
        return True
    
    def alphaNum(self, c):
        return(
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
        