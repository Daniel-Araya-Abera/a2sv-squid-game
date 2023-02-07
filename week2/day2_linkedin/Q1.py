# Crawler Log Folder
# https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../" and depth > 0:
                depth -= 1
            elif log != "./" and log != "../":
                depth += 1
        return depth

# class Solution:
    # def minOperations(self, logs: List[str]) -> int:
    #     stack = []
    #     for log in logs:
    #         if log == "../" and stack:
    #             stack.pop()
    #         elif log != "./" and log != "../":
    #             stack.append(log)
    #     return len(stack)
