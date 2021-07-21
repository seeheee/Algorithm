
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[0] * n for _ in range(m)]

        # print(visited)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    visited[0][0] = 1
                else:
                    # print(visited[-1][1])
                    visited[i][j] = visited[i][j-1] + visited[i-1][j]
        return visited[m-1][n-1]




if __name__ == '__main__':
    print(Solution().uniquePaths(3,7))