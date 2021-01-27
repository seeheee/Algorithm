from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
check = [[False]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    que = deque()
    # 칸을 셀 때에는 시작 위치도 포함되므로 1로 초기화 필수
    que.append((0,0))
    check[0][0] = True
    dist[0][0] = 1

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and check[nx][ny] == False:
                    que.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    check[nx][ny] = True
    else:
        # que가 비워져있으면 맨 마지막에 담긴 배열 출력
        print(dist[N-1][M-1])


bfs()
