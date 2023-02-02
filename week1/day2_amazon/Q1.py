# Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        while idx < len(nums) and nums[idx] == 0:
            idx += 1
        
        res = 0
        while idx < len(nums):
            amount = nums[idx]
            for i in range(idx, len(nums)):
                nums[i] -= amount
            
            while idx < len(nums) and nums[idx] == 0:
                idx += 1
            res += 1
        return res
