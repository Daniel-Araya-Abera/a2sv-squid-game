# Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_size = len(pref)
        count = sum([1 if word[:prefix_size] == pref else 0 for word in words])
        return count
    
# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         prefix_size = len(pref)
#         count = 0
#         for word in words:
#             if pref == word[: prefix_size]:
#                 count += 1
#         return count
