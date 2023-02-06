# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        res = 0
        memo = {}
        words = set(words)
        for i, word in enumerate(words):
            res = max(res, self.dfs(word, words, memo))
        return res
    
    def dfs(self, curr_word, words, memo):
        state = curr_word
        if state in memo:
            return memo[state]
        
        best = 0
        for insert_idx in range(len(curr_word) + 1):
            for i in range(26):
                new_char = chr(i + ord('a'))
                possible_next_word = curr_word[:insert_idx] + new_char + curr_word[insert_idx:]
                if possible_next_word in words:
                    best = max(best, self.dfs(possible_next_word, words, memo))
        
        res = best + 1
        memo[state] = res
        return res

'''
time -> O(n * word_len * 26), word_len = 16
space -> O(n)

Constraints:
-> 1 <= words.length <= 1000
-> 1 <= words[i].length <= 16
-> words[i] only consists of lowercase English letters.
'''
