from collections import deque


def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    r = len(maps)
    c = len(maps[0])
    # 올바른 방법
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    visited = [[0] * c for _ in range(r)]
    print(visited)

    # 인덱스 에러가 난 이유
    # [[0], [0], [0], [0], [0]]
    wrong_visited = [[0 * r] for _ in range(r)]
    print(wrong_visited)

    visited[0][0] = 1
    que = deque()
    que.append([0, 0])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == 1:
                    if visited[nx][ny] == 0:
                        # print(nx, ny)
                        visited[nx][ny] = visited[x][y] + 1
                        que.append([nx, ny])

    if visited[r-1][c-1] == 0:
        return -1
    else:
        return visited[r-1][c-1]





print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))