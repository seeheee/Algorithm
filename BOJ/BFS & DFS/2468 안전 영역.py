from collections import deque
N = int(input())
Area_list = list(list(map(int, input().split())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and Area_list[nx][ny] > h:
                visited[nx][ny] = 1
                bfs(nx, ny, h)

print(list(map(max, Area_list))) #[8, 6, 7, 7, 9]

ans = 1
for k in range(1, max(map(max, Area_list))):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if Area_list[i][j] > k and visited[i][j] == 0:
                safe += 1
                visited[i][j] = 1
                bfs(i, j, k)
    ans = max(ans, safe)

print(ans)


# que = deque()
# for a in range(N):
#     for b in range(N):
#         que.append([a, b])
# for i in Area_list:
#     Area_min = min(i)
#     Area_max = max(i)
#
# for j in range(Area_min, Area_max+1):
#     bfs(j)