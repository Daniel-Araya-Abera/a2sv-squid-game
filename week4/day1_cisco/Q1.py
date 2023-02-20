# Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        res = 0
        for i in range(1, len(nums)):
            curr_num = nums[i]
            diff = nums[i] - min_so_far
            res = max(res, diff)
            min_so_far = min(min_so_far, curr_num)
        
        return res if res > 0 else -1
