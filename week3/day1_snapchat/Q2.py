# Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: #
            return -1

        n = len(grid)
        neighbours = ((1,0),(0,1),(1,1),(-1,0),(-1,1),(0,-1),(-1,-1),(1,-1))
        queue = deque([(0,0,1)])
        visited = set([(0,0)])        

        while queue:
            curr_i, curr_j, curr_count = queue.popleft()
            if curr_i == n - 1 and  curr_j == n - 1:
                return curr_count

            for x, y in neighbours:
                new_i, new_j = curr_i + x, curr_j + y
                if self.inbound(new_i, new_j, n):
                    if grid[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                        queue.append((new_i, new_j, curr_count + 1))
                        visited.add((new_i, new_j))
        return -1
    
    def inbound(self, i, j, n):
        return 0 <= i < n and 0 <= j < n
