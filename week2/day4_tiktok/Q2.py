# Maximum Swap
# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        sorted_digits = sorted(digits, reverse = True)
        n = len(digits)
        for i in range(n):
            if digits[i] != sorted_digits[i]:
                self.swapItems(digits, sorted_digits[i], i)
                break
        return int("".join(digits))
                
    def swapItems(self, digits, target, i):
        idx = len(digits) - 1
        while idx >= i:
            if target == digits[idx]: 
                digits[i], digits[idx] = digits[idx], digits[i]
                break
            idx -= 1
        return digits
