# Best Team With No Conflicts
# https://leetcode.com/problems/best-team-with-no-conflicts/
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        people = sorted([(ages[i], scores[i]) for i in range(n)])
        # people.append((float('inf'), float('inf')))

        # dp = [0] * n
        # for i in range(n - 1, -1 , -1):

        memo = {}
        best = 0
        for i in range(n - 1, -1, -1):
            best = max(best, self.dfs(i, people, memo))
        return best

    def dfs(self, idx, people, memo):
        if idx < 0:
            return 0
        state = idx
        if state in memo:
            return memo[state]
        
        best = 0
        for i in range(idx - 1, -1, -1):
            if people[i][0] == people[idx][0] or people[i][1] <= people[idx][1]:
                #same age or less score(with less idx)
                best = max(best, self.dfs(i, people, memo))

        #take curr_score
        res = best + people[idx][1]
        memo[state] = res
        return res
