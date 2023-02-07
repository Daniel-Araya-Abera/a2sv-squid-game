# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         for i, num in enumerate(nums):
#             if len(heap) < k:
#                 heapq.heappush(heap, num)
#             else:
#                 if num > heap[0]:
#                     heapq.heapreplace(heap,num)
#         return heap[0]
