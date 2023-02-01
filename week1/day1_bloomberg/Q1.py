# Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        prefix = [0] * n

        for i, block in enumerate(blocks):
            white_count = prefix[i - 1] if i - 1 >= 0 else 0
            if block == "W":
                white_count += 1
            prefix[i] = white_count
        
        start, end = 0, k - 1
        res = float('inf')
        while end < len(prefix):
            count = prefix[end]
            start = end - k
            if start >= 0:
                count -= prefix[start]
            res = min(res, count)
            end += 1

        return res
