# String Compression II
# https://leetcode.com/problems/string-compression-ii/description/
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return self.helper(s, 0, k, '*', 0, {})
    
    def helper(self, s, idx, remaining_k, prev_char, prev_count, memo):
        if idx == len(s):
            return self.getCost(prev_count)
        
        state = (idx, remaining_k, prev_char, prev_count)
        if state in memo:
            return memo[state]
        
        #take current char
        take = float('inf')
        if prev_char == s[idx]:
            take = self.helper(s, idx + 1, remaining_k, prev_char, prev_count + 1, memo)
        else:
            curr_cost = self.getCost(prev_count)
            take = curr_cost + self.helper(s, idx + 1, remaining_k, s[idx], 1, memo)

        #skip currrent char
        skip = float('inf')
        if remaining_k > 0:
            skip = self.helper(s, idx + 1, remaining_k - 1, prev_char, prev_count, memo)
        
        res = min(take, skip)
        memo[state] = res
        return res
    
   
    def getCost(self, prev_count):
        if prev_count == 0 or prev_count == 1:
            return prev_count
        return len(str(prev_count)) + 1 #char + digits' count/length
