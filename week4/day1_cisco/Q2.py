# Expressive Words
# https://leetcode.com/problems/expressive-words/
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        
        stack = self.getStack(s)
        for word in words:
            if self.isValid(word, stack):
                res += 1
        
        return res
    
    
    def getStack(self, s):
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
        return stack
    
    def isValid(self, word, stack1):
        stack2 = self.getStack(word)
        
        if len(stack1) != len(stack2):
            return False
        
        for i in range(len(stack1)):
            item1, item2 = stack1[i], stack2[i]
            
            if item1[0] != item2[0]:
                return False
            #same chars
            if item1[1] < 3 and item1[1] != item2[1]:
                return False
            if item1[1] < item2[1]:
                return False
        return True
