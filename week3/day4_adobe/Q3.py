# Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        nums_freq = collections.defaultdict(int)
        for i, num in enumerate(changed):
            nums_freq[num] += 1
        
        res = []
        for i, num in enumerate(changed):
            double_num = 2 * num
            if nums_freq[double_num] > 0 and nums_freq[num] > 0:
                nums_freq[double_num] -= 1
                nums_freq[num] -= 1
                res.append(num)
        
        for key in nums_freq:
            if nums_freq[key] != 0:
                return []

        return res
