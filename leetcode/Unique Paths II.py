
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        N, M = len(obstacleGrid), len(obstacleGrid[0])
        d = [[0]*M for _ in range(N)]

        # 로봇이 맨 처음으로 가는 수(초기값 설정)
        d[0][0] = 1

        for i in range(N):
            for j in range(M):
                # 1이면 장애물이므로 경우의 수가 없음
                if obstacleGrid[i][j] == 1:
                    # 결과를 담는 좌표는 경우의 수가 0
                    d[i][j] = 0
                else:
                    # 로봇이 갈 수 있는 경우의 수는 2가지이기 때문(오른쪽이거나 밑으로)
                    # 그러면 현재 좌표는 위에서 오거나 왼쪽에서 온 좌표를 더하면 됨
                    if i > 0:
                        d[i][j] += d[i-1][j] #내 위에 있는 수를 더함
                    if j > 0:
                        d[i][j] += d[i][j-1] #내 왼쪽에 있는 수 더함
        return d[N-1][M-1]