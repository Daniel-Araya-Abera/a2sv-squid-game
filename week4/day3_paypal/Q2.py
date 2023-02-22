# Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description/
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        count = 0
        while True:
            swap_present = self.performSwaps(s)
            if not swap_present:
                break
            count += 1
            
        return count
    
    def performSwaps(self, s):
        swaps = {}
        for i in range(len(s) - 1, -1, -1):
            if "".join(s[i:i + 2]) == "01":
                swaps[i] = i + 1
        
        for key, value in swaps.items():
            s[key], s[value] = s[value], s[key]
        
        # return len(swaps.keys) > 0
        return len(swaps.keys()) > 0

'''
brute force
time -> O(N^2)
'''
    
'''
"001100111"
"001100001110"
'''
