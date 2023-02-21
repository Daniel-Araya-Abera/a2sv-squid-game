# Mini Parser
# https://leetcode.com/problems/mini-parser/
###Interface code 
### ...
class Solution:
    def resolveDigit(self, s):
        return NestedInteger(int(s))

    def deserialize(self, s: str) -> NestedInteger:
        if s[0].isdigit() or s[0] == "-":
        # if s[0] != "[":
            return self.resolveDigit(s)
        
        stack = []
        i = 0
        is_negative = False
        while i < len(s):
            char = s[i]
            if char == "[":
                stack.append("[")
                i += 1
            elif char == "-": #negative
                is_negative = True
                i += 1
            elif char.isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if is_negative:
                    num *= -1
                    is_negative = False
                stack.append(num)
            elif char == "]":
                top = []
                while stack and stack[-1] != "[":
                    top.append(stack.pop())
                stack.pop() #"[" element
                top.reverse()
                stack.append(top)
                i += 1
            else: #comma
                i += 1

        return self.convertToNestedInteger(stack[0])
    
    def convertToNestedInteger(self, curr_item):
        if type(curr_item) == type([]):
            res = NestedInteger()
            for single_item in curr_item:
                res.add(self.convertToNestedInteger(single_item))
            return res
        return NestedInteger(curr_item)

'''
"[324,[]]"
"[324]"
'''