
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])

        dp = [[0]*N for _ in range(M)]

        for i in range(M):
            for j in range(M):
                if matrix[i][j] == 1:
                    dp[i][j] += dp[i][j]