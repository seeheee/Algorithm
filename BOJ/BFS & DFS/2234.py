# 성곽(골드 4)
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
give = [list(map(int, input().split())) for _ in range(M)]
visit = [[0]*N for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


que = deque()
def bfs(x, y):
    cnt = 1
    que.append([x, y])
    visit[x][y] = 1 # que의 값이 1이어야 while문 안으로 들어감
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visit[nx][ny] == 0:
                if k == 0:
                    if 1 & give[x][y]: continue
                elif k == 1:
                    if 2 & give[x][y]: continue
                elif k == 2:
                    if 4 & give[x][y]: continue
                elif k == 3:
                    if 8 & give[x][y]: continue
                visit[nx][ny] = 1
                que.append([nx, ny])
                cnt += 1 # 제일 큰 방 알기 위해서
    return cnt
# 이 성에 있는 방의 개수 세기 (기본)
result1 = 0
result2 = 0
result3 = 0
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            result1 += 1
            result2 = max(result2, bfs(i,j))
print(result1)
print(result2)

for i in range(M):
    for j in range(N):
        num = 1
        while num < 9:

            if num & give[i][j]:
                visit = [[0] * N for _ in range(M)]
                give[i][j] -= num
                result3 = max(result3, bfs(i, j))
                give[i][j] += num
            num *= 2
print(result3)