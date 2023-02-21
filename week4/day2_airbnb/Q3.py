# Mini Parser
# https://leetcode.com/problems/mini-parser/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

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