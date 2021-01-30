# 이 문제 너무 어려워...
# 추가적으로 고려해야 할 상황
# 2차원 배열에 0이 한개라도 있는 경우(익지 않은 토마토가 있다)
# 모두 1인 경우(애초에 모두 익은 토마토가 들어간 경우)

from collections import deque
M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    que = deque()

    que.append((x, y))
    print(que)
    while que:
        x1, y1 = que.popleft()
        for n in range(4):
            nx = x1 + dx[n]
            ny = y1 + dy[n]
            if 0 <= nx < N and 0 <= ny < M:
                if farm[nx][ny] == 0:
                    farm[nx][ny] = farm[x1][y1] + 1
                    que.append((nx, ny))


for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            bfs(i, j)
            print(bfs(i,j))

# 2차원 배열의 값이 0이면 모두 익지 않은 것이므로 1로 초기화
Not_Cook = 1
result = -1

for k in farm:
    for el in k:
        print("원소 꺼내기", el)
        if el == 0:
            Not_Cook = 0
        result = max(result, el)

if Not_Cook == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)