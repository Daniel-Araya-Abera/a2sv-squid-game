# Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_prefix = [0] * n
        b_prefix = [0] * n #
        
        for i, char in enumerate(s):
            a_freq = 0
            b_freq = 0
            if i - 1 >= 0:
                a_freq = a_prefix[i - 1]
                b_freq = b_prefix[i - 1]
            if char == "a":
                a_freq += 1
            else:
                b_freq += 1
            
            a_prefix[i] = a_freq
            b_prefix[i] = b_freq
        
        res = n
        for i in range(n):
            left_b = b_prefix[i - 1] if i - 1 >= 0 else 0
            right_a = a_prefix[n - 1] - a_prefix[i]
            res = min(res, left_b + right_a)
        
        return res
