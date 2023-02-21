# Shortest Path to Get All Keys
# https://leetcode.com/problems/shortest-path-to-get-all-keys/
'''
Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
** Not all keys are present, we return all keys for the locks that exist
'''
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        starting_points = []
        total_keys = 0
        equilibrium = [0,0,0,0,0,0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    starting_points.append((i,j))
                elif grid[i][j] in "abcdef": #key/lowercase
                    total_keys += 1
        
        if len(starting_points) == 0: # ["BaA.."]
            return -1
        
        neighbours = ((1,0), (0,1), (-1,0), (0,-1))
        # best = float('inf')
        best = -1
        for pt in starting_points:
            moves = self.bfs(pt, m, n, grid, neighbours, total_keys)
            best = max(best, moves)
        return best
    
    def bfs(self, pt, m, n, grid, neighbours, total_keys):
        start_i, start_j = pt
        queue = deque([(start_i, start_j, set(), 0)])
        visited = set([(start_i, start_j, "")])
        while queue:
            curr_state = queue.popleft()
            i, j, curr_keys, curr_steps = curr_state
            if len(curr_keys) == total_keys:
                return curr_steps
            
            for x,y in neighbours:
                new_i, new_j = i + x, j + y
                if self.inbound(new_i, new_j, m, n):
                    item = grid[new_i][new_j]
                    copied_keys = set(list(curr_keys))
                    if item.isalpha() and item.lower() == item: #small letter
                        copied_keys.add(item)
                    
                    new_state = (new_i, new_j, tuple(sorted(copied_keys)))
                    if self.isValid(new_i, new_j, curr_state, grid) and (new_state) not in visited:
                        visited.add((new_state))
                        queue.append((new_i, new_j, copied_keys, curr_steps + 1))
        return -1
    
    def inbound(self, x, y, row_size, col_size):
        return 0 <= x < row_size and 0 <= y < col_size
    
    def isValid(self, new_i, new_j, curr_state, grid):
        i, j, curr_keys, curr_steps = curr_state
        curr_item = grid[new_i][new_j]
        if curr_item == "#":
            return False
        if curr_item == "@": #?
            return True
        if curr_item.isalpha():
            if curr_item.upper() == curr_item: #capital
                return curr_item.lower() in curr_keys
            return True
        # it's a "." or empty cell
        return True
            
