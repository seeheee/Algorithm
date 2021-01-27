from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
house = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def bfs(x, y):
    que = deque()
    que.append((x, y))
    cnt = 1
    house[i][j] = 0
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if house[nx][ny] == 1:
                    que.append((nx,ny))
                    cnt += 1
                    house[nx][ny] = 0
    else:
        result.append(cnt)
        result.sort()
        return result


count = 0
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            count += 1
            bfs(i, j)


print(count)

for n in result:
    print(n)
