# Restore the Array From Adjacent Pairs
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        for node in graph:
            if len(graph[node]) == 1: #one end of the list
                return self.bfs(node, graph)
        return []
    
    def bfs(self, node, graph):
        res = [node]
        visited = set([node])
        queue = deque([node])
        while queue:
            curr_node = queue.popleft()
            for neighbour in graph[curr_node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    res.append(neighbour)
        
        return res
