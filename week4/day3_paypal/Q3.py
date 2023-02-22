# Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainings = collections.defaultdict(int)
        res = 0
        for curr_song in time:
            curr_extra = curr_song % 60
            # curr_remaining = 60 - curr_extra
            curr_remaining = (60 - curr_extra) % 60
            res += remainings[curr_remaining]
            remainings[curr_extra] += 1
        
        return res
