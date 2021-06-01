from collections import deque
N = int(input())

visited = [[0 for _ in range(N)] for _ in range(N)]
Area_list = list(list(map(int, input().split())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(j):
    count = 0
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and Area_list[nx][ny] > j:
                    visited[nx][ny] = 1
                    que.append([nx, ny])
        count += 1
    return count

que = deque()
for a in range(N):
    for b in range(N):
        que.append([a, b])


for i in Area_list:
    Area_min = min(i)
    Area_max = max(i)

for j in range(Area_min, Area_max+1):
    bfs(j)
