# Simplify Path
# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for item in path:
            if item != "":
                if item == "..":
                    if stack:
                        stack.pop()
                elif item == ".":
                    continue
                else:
                    stack.append(item)
        
        return "/" + "/".join(stack)
