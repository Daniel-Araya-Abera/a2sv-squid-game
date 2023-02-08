# Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if len(heap) < 3:
                if not heap or heap[0] != num:
                    heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
        
        return heap[0] if len(heap) == 3 else max(heap)
