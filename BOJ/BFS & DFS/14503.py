from collections import deque
import sys
input = sys.stdin.readline

# N = 세로(열), M = 가로(행)
N, M = map(int, input().split())
r, c, d = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(M)]

que = deque()

# 북 동 남 서 (0,1,2,3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change(d):
    # 북쪽일 경우 서쪽으로
    if d == 0:
        return 3
    # 동쪽일 경우 북쪽
    elif d == 1:
        return 0
    # 남쪽일 경우 동쪽
    elif d == 2:
        return 1
    # 서쪽일 경우 남쪽
    elif d == 3:
        return 2

def back(d):
    # 북쪽이면 남쪽으로 한칸 후진
    if d == 0:
        return 2
    # 서쪽->동쪽
    elif d == 3:
        return 1
    # 남쪽 -> 북쪽
    elif d == 2:
        return 0
    # 동쪽 -> 서쪽
    elif d == 1:
        return 3

def bfs(x, y, dir):
    count = 1
    que.append([x, y, dir])
    state[x][y] = 2
    while que:
        x, y, dir = que.popleft()
        temp = dir
        for i in range(4):
            temp = change(temp)
            nx, ny = x + dx[temp], y + dy[temp]
            if 0 <= nx < M and 0 <= ny < N and state[nx][ny] == 0:
                state[nx][ny] = 2
                que.append([nx, ny, temp])
                count += 1
                break

            # 사방에 갈 곳이 없는 경우
            if i == 3:
                nx, ny = x + dx[back(dir)], y + dy[back(dir)]
                que.append([nx, ny, dir])

                # 뒷 칸도 벽인 경우
                if state[nx][ny] == 1:
                    return count


print(bfs(r, c, d))
