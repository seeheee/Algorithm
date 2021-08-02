from collections import deque


def solution(n, m, image):
    visited = [[0] * (m) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    que = deque()

    def bfs(i, j):
        que.append([i, j])
        while que:
            x, y = que.popleft()
            visited[x][y] = 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if image[x][y] == image[nx][ny]:
                        visited[nx][ny] = 1
                        que.append([nx, ny])

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:  # 방문을 했으면 들어가면 안된다.(이걸안하면 개수 그대로 전부 들어감)
                bfs(i, j)
                answer += 1

    return answer


# from collections import deque
#
#
# def solution(n, m, image):
#     visited = [[0] * (m) for _ in range(n)]
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     answer = 0
#     que = deque()
#
#     def bfs(i, j):
#         que.append([i, j])
#         while que:
#             x, y = que.popleft()
#             visited[x][y] = 1
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
#                     if image[x][y] == image[nx][ny]:
#                         visited[nx][ny] = 1
#                         que.append([nx, ny])
#
#     for i in range(n):
#         for j in range(m):
#             bfs(i, j)
#             answer += 1
#
#     return answer




print(solution(2,	3,	[[1, 2, 3], [3, 2, 1]]	))