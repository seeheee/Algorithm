from collections import deque
import sys

TC = int(input())

for _ in range(TC):
    N, M, XY = map(int, input().split())
    farm = [list(0 for _  in range(M)) for _ in range(N)]

    # 상하좌우의 좌표를 초기화
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x1, y1):
        que = deque()
        que.append((x1, y1))
        farm[i][j] = 0
        while que:
            x1, y1 = que.popleft()
            for k in range(4):
                nx = x1 + dx[k]
                ny = y1 + dy[k]
                if 0 <= nx <M and 0 <= ny < N:
                    if farm[i][j]:
                        que.append((i, j))
                        farm[i][j] = 0
        else:
            return

    count = 0
    for _ in range(XY):
        x, y = map(int, input().split())
        for i in range(M):
            for j in range(N):
                if i == x and j == y:
                    farm[i][j] = 1
                    if farm[i][j]:
                        count += 1
                        bfs(i, j)


    print(count)