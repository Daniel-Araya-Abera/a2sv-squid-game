# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        for i, weight in enumerate(w):
            prev_sum = self.prefix[i - 1] if i - 1 >= 0 else 0
            curr_sum = prev_sum + weight
            self.prefix.append(curr_sum)
        
    def pickIndex(self) -> int:
        min_element = 1
        max_element = self.prefix[-1]
        target = random.randint(min_element, max_element)
        return self.binarySearch(target, self.prefix)
    

    def binarySearch(self, target, prefix):
        start, end = 0, len(prefix) - 1
        res_idx = end
        while start <= end:
            mid = start + (end - start) // 2
            # if target >= prefix[mid]:
            if target > prefix[mid]:
                start = mid + 1
            else:
                res_idx = mid
                end = mid - 1

        return res_idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()