# 결혼식 문제 이해 안됨
from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

friends = [[] for _ in range(N)]

def bfs(x):
    que = deque()
    visited = [0] * N # 방문 확인하기 위한 리스트 0으로 초기화
    visited[x] = 1
    que.append(x)
    while que:
        p = que.popleft()
        for i in friends[p]:
            if not visited[i]:
                visited[i] = visited[p] + 1
                print(i, visited[i])
                que.append(i)
                print("que", que)
    else:
        return visited


for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

count = 0
param = bfs(0)
for answer in param:
    if 1 < answer <=3:
        count += 1
print(count)