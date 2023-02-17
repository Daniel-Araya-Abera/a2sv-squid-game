# Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        minFoundIndices = collections.defaultdict(list)
        maxFoundIndices = collections.defaultdict(list)
        otherValidsFoundIndices = []
        
        for i, num in enumerate(nums):
            if minK <= num <= maxK:
                if num == minK:
                    minFoundIndices[num].append(i)
                if num == maxK:
                    maxFoundIndices[num].append(i)
                if num != minK and num != maxK:
                    otherValidsFoundIndices.append(i)
                
                #calculate
                minIndices = minFoundIndices[minK]
                maxIndices = maxFoundIndices[maxK]
                size1, size2 = len(minIndices), len(maxIndices) 
                if size1 > 0 and size2 > 0:
                    maxStart = min(minIndices[-1], maxIndices[-1])
                    minStart = min(minIndices[0], maxIndices[0])
                    if len(otherValidsFoundIndices) > 0:
                        minStart = min(minStart, otherValidsFoundIndices[0])
                    
                    res += (maxStart - minStart + 1)
            else:
                while len(minFoundIndices[minK]) > 0:
                    minFoundIndices[minK].pop()
                while len(maxFoundIndices[maxK]) > 0:
                    maxFoundIndices[maxK].pop()
                while len(otherValidsFoundIndices) > 0:
                    otherValidsFoundIndices.pop()
        return res
