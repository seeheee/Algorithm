from collections import deque
N = int(input())

visited = [[0 for _ in range(N)] for _ in range(N)]
list1 = list(list(map(int, input().split())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    count = 0
    que = deque()
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and list1[nx][ny] > :
                        visited[nx][ny] = 1
                        que.append([nx, ny])
            count += 1
    return count
