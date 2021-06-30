# 최단 경로를 구하는 문제는 BFS 이용
from collections import deque

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0])  # 이거 어떻게 할지 생각 못 함(열)

    # 동, 서, 남, 북
    dx = [[1,0], [-1, 0], [0,1], [0,-1]]

    visited = [[0 * m] for _ in range(n)]

    que = deque()
    que.append([0, 0])
    visited[0][0] = 1
    while que:
        y, x = que.popleft()
        for k in range(4):
            ny = y + dx[k][0]
            nx = x + dx[k][1]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1:
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x] + 1
                        que.append([ny, nx])
    return visited[n-1][m-1]

    #
    # for i in range(n):
    #     for j in range(m):
    #         if maps[i][j] == 1:
    #             bfs(i, j)


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# maps = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for i in range(3):
#     for j in range(4):
#         print(i, j, maps[i][j])