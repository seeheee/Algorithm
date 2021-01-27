# BFS의 기본 문제

from collections import deque

N, M = map(int, input().split())
images = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우의 좌표를 초기화
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

size_list = []

def bfs(x,y):
    que = deque()
    que.append((x,y))
    images[i][j] = 0  # 한번 들어온 이미지이기에 다시 들어올 경우를 막기 위해 0으로 초기화
    size = 1  # 그림의 크기를 담기 위해서 초기화
    while que:
        x, y = que.popleft()
        for k in range(4): # 좌표 돌아가면서 확인
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if images[nx][ny] == 1:
                    que.append((nx,ny))
                    size += 1  # que가 있다는 것은 그림이라는 것으로 크기를 계속 더한다.
                    images[nx][ny] = 0  # 다시 탐색되는 것을 막기위해 탐색한 것을 명시
    else:
        size_list.append(size)
        return



count = 0  # 그림의 개수를 담기 위한 것
for i in range(N):
    for j in range(M):
        if images[i][j] == 1:
            count += 1
            bfs(i, j)

print(count)
if size_list:
    print(max(size_list))
else:
    print("0")