from collections import deque
import sys
input = sys.stdin.readline
TC = int(input().rstrip())

for _ in range(TC):
    M, N, XY = map(int, input().rstrip().split())
    farm = [list(0 for _  in range(N)) for _ in range(M)]
    # print("farm 초기화" , farm)
    # 상하좌우의 좌표를 초기화
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x1, y1):
        que = deque()
        que.append((x1, y1))
        farm[a][b] = 0
        while que:
            x1, y1 = que.popleft()
            for k in range(4):
                nx = x1 + dx[k]
                ny = y1 + dy[k]
                if 0 <= nx < M and 0 <= ny < N:
                    if farm[nx][ny]:
                        que.append((nx, ny))
                        farm[nx][ny] = 0
        else:
            return

    count = 0
    for _ in range(XY):
        x, y = map(int, input().rstrip().split())
        for i in range(M):
            for j in range(N):
                if i == x and j == y:
                    farm[i][j] = 1

    # print("farm", farm)

    for a in range(M):
        for b in range(N):
            if farm[a][b] == 1:
                count += 1
                bfs(a, b)
    print(count)