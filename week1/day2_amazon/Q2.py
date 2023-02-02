# Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        ones = [0] * n
        for i, char in enumerate(s):
            curr_count = ones[i - 1] if i - 1 >= 0 else 0
            if char == "1":
                curr_count += 1
            ones[i] = curr_count
        
        res = 0
        for i in range(1, n - 1): 
            #middle indices, searching for 010 & 101
            if s[i] == "0": 
                #searching 101
                left_ones = ones[i - 1]
                right_ones = ones[n - 1] - ones[i]
                res += left_ones * right_ones
            elif s[i] == "1":
                #searching 010
                left_zeros = i - ones[i - 1] # i number of elements - number of 1s
                right_zeros = (n - 1 - i) - (ones[n - 1] - ones[i]) # n - i - 1 number of elements
                res += left_zeros * right_zeros
        return res
