# Matrix Block Sum
# https://leetcode.com/problems/matrix-block-sum/
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        prefix = [[mat[i][j] for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(1, col):
                prefix[i][j] += prefix[i][j - 1]
        
        for i in range(1, row):
            for j in range(col):
                prefix[i][j] += prefix[i - 1][j]
        
        res = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                start_i, start_j = max(i - k, 0), max(j - k, 0)
                end_i, end_j = min(i + k, row - 1), min(j + k, col - 1)
                curr_res = prefix[end_i][end_j]
                if start_j - 1 >= 0:
                    curr_res -= prefix[end_i][start_j - 1]

                if start_i - 1 >= 0:
                    curr_res -= prefix[start_i - 1][end_j]

                if start_i - 1 >= 0 and start_j - 1 >= 0:
                    curr_res += prefix[start_i - 1][start_j - 1]
                res[i][j] = curr_res
        
        return res
