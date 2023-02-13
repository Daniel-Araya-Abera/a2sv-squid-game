# Add Binary
# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_size, b_size = len(a), len(b)
        max_len = max(a_size, b_size)
        a = "0" * (max_len - a_size) + a
        b = "0" * (max_len - b_size) + b
        return self.helper(a, b)
    
    def helper(self, a, b):
        i = len(a) -  1
        res = [0] * len(a)
        carry = 0
        while i >= 0:
            curr_sum = int(a[i]) + int(b[i]) + carry
            carry, curr_sum = self.getSumAndCarry(curr_sum)
            res[i] = str(curr_sum)
            i -= 1
        
        return "".join(res) if carry == 0 else "1" + "".join(res)

    def getSumAndCarry(self, curr_sum):
        if curr_sum == 0:
            return 0, 0
        elif curr_sum == 1:
            return 0, 1
        elif curr_sum == 2:
            return 1, 0
        return 1, 1
