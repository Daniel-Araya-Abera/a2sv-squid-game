# Number of Pairs of Strings With Concatenation Equal to Target
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        count = 0
        seen = collections.defaultdict(int)
        for digit_str in nums:
            seen[digit_str] += 1
        
        target_len = len(target)
        for i in range(target_len - 1):
            first_part = target[:i + 1]
            second_part = target[i + 1:]
            freq1 = seen[first_part]
            freq2 = seen[second_part]
            if first_part == second_part:
                count += freq1 * (freq2 - 1)
            else:
                count += freq1 * freq2
        
        return count
            

# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         n = len(nums)
#         count = 0
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     concatenated = nums[i] + nums[j]
#                     if concatenated == target:
#                         count += 1
#         return count
