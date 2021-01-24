# 기존의 좌표에 대각선 좌표까지 생각하기
from collections import deque

while True:

    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    land_sea = [list(map(int, input().split())) for _ in range(M)]

    dx = [-1, 0, 1, 0, 1, -1, -1, 1]
    dy = [0, -1, 0, 1, 1, 1, -1, -1]

    def bfs(x, y):
        que = deque()
        que.append((x, y))
        land_sea[i][j] = 0
        while que:
            x, y = que.popleft()
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N:
                    if land_sea[nx][ny] == 1:
                        que.append((nx, ny))
                        land_sea[nx][ny] = 0
        else:
            return

    count = 0
    for i in range(M):
        for j in range(N):
            if land_sea[i][j] == 1:
                count += 1
                bfs(i, j)

    print(count)