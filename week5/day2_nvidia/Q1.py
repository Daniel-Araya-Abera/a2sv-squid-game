# Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        max_freq = max(collections.Counter(nums).values()) #max_freq = target

        res = n # res = float('inf')
        freq = collections.defaultdict(int)
        while right < n:
            curr_num = nums[right]
            freq[curr_num] += 1
            # while freq[curr_num] == target:
            while freq[curr_num] == max_freq:
                res = min(res, right - left + 1)
                freq[nums[left]] -= 1
                left += 1
            right += 1 

        return res
