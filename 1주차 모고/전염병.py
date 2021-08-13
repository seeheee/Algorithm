# 생각못한 테스트케이스
# 2, 3, [[1, 1], [1, 2]], [[2, 1], [2, 2], [2, 3]]


from collections import deque

def solution(m, n, infests, vaccinateds):
    office = [[0] * (n + 1) for _ in range(m + 1)]
    visited = [[0] * (n + 1) for _ in range(m + 1)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    l = m * n - len(infests) - len(vaccinateds)
    if l == 0:
        return 0

    # for a, b in infests:
    #     visited[a][b] = 1

    def bfs():
        while que:
            x, y = que.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 1 <= nx <= m and 1 <= ny <= n:
                    if visited[nx][ny] == 0 and office[nx][ny] == 0:
                        office[nx][ny] = office[x][y] + 1
                        visited[nx][ny] = 1
                        que.append([nx, ny])

    que = deque()
    for i, j in infests:
        que.append([i, j])
        visited[i][j] = 1

    for a, b in vaccinateds:
        office[a][b] = 1

    bfs()

    # answer = 0
    # result = max(max(office))
    #
    # for v in visited:
    #     answer += v.count(1)
    # print(visited)
    result = max(map(max, office))
    # answer = sum(visited, []).count(0)

    if sum(visited, []).count(1) < m * n - len(vaccinateds):
        return -1
    else:
        return result

print(solution(2,	3,[[2,2]],[[1,2],[2,1],[2,3]]))