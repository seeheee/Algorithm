from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 3차원 배열 표현
tomato_list = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(z, x, y):
    que = deque()
    que.append([z, x, y])
    while que:
        z, x, y = que.popleft()
        visited[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if tomato_list[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    # 경로의 길이를 세는 방법(가지수 세는 법)
                    # tomato_list[z][x][y] 값이 1이라서 결과에 -1을 해 줘야함
                    tomato_list[nz][nx][ny] = tomato_list[z][x][y] + 1
                    visited[nz][nx][ny] = 1
                    que.append([nz, nx, ny])



for j in range(H):
    for k in range(N):
        for l in range(M):
            if tomato_list[j][k][l] == 1 and visited[j][k][l] == 0:
                visited[j][k][l] = 1
                bfs(j, k, l)


############### 이 부분 생각 못함 ##################
# bfs 함수를 모두 돌고 난 후 예외처리와 결과 출력
# 만약 저장될 때부터 모든 토마토가 익어있는 상태면 0을 출력
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력

# x값에는 -1, 0, 1 그리고 그 이상 숫자가 들어갈 수 있으므로 -1을 초기값으로 설정
result = -1
Is_true = False
for z in tomato_list:
    for y in z:
        for x in y:
            if x == 0:
                Is_true = True
            # tomato_list 안에서 모든 원소를 돌면서 큰 값을 저장하면서 비교해서 찾는다.
            result = max(result, x)

if Is_true:  # x에 0이 하나라도 있다는 것은 안 익은게 있다는 뜻
    print(-1)
elif result == 1:  # 가장 큰 값이 1이라는 것은 모두 익어있는 상태라는 뜻
    print(0)
else:
    print(result - 1)

