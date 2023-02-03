# Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                check1 = self.isPalindrome(s, start + 1, end)
                check2 = self.isPalindrome(s, start, end - 1)
                return check1 or check2
            start += 1
            end -= 1
        
        return True
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
