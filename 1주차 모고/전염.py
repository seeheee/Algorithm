# 테케 2개 통과 못함

from collections import deque
def solution(m, n, infests, vaccinateds):
    office = [[0] * (n + 1) for _ in range(m + 1)]
    visited = [[0] * (n + 1) for _ in range(m + 1)]
    # ha = [[0] * (n + 1) for _ in range(m + 1)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    l = m*n - len(infests) - len(vaccinateds)
    if l == 0:
        return 0

    def bfs():
        while que:
            x, y = que.popleft()
            visited[x][y] = 1
            # print(x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # print(nx,ny)
                if 1 <= nx <= m and 1 <= ny <= n:
                    if visited[nx][ny] == 0 and office[nx][ny] == 0:
                        office[nx][ny] = office[x][y] + 1
                        visited[nx][ny] = 1
                        que.append([nx, ny])
        return visited

    for a, b in vaccinateds:
        office[a][b] = 1

    que = deque()
    for i, j in infests:
        que.append([i, j])

    bfs()

    result = max(map(max, office))
    if result == 1:
        return -1
    else:
        return result