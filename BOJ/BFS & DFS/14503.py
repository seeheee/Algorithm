from collections import deque
import sys
input = sys.stdin.readline

# N = 세로(열), M = 가로(행)
N, M = map(int, input().split())
r, c, d = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(M)]
visit = [[0]*N for _ in range(M)]

que = deque()

def bfs(x, y, dir):
    count = 1
    que.append([x, y, d])
    visit[x][y] = 1
    while que:
        x, y, dir = que.popleft()
        if dir == 0:
            for i in range(4):
                nx = x + Ndx[i]
                ny = y + Ndy[i]
        elif dir == 1:
            for i in range(4):
                nx = x + Edx[i]
                ny = y + Edy[i]
        elif dir == 2:
            for i in range(4):
                nx = x + Sdx[i]
                ny = y + Sdy[i]
        elif dir == 3:
            for i in range(4):
                nx = x + Wdx[i]
                ny = y + Wdx[i]
                if 0 <= nx < M and 0 <= ny < N:
                    visit[nx][ny] = 1
                    que.append([nx, ny])
                    count += 1
    return count


bfs(c, r, d)
