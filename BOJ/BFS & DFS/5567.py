# 결혼식 문제 이해 안됨
from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

invite = [list(map(int, input().rstrip().split())) for _ in range(1, M+1)]

check = [False] * M

#
# print("invite 배열", invite[0])
# print("check 배열", check)

def bfs(invite, start, check):
    que = deque()
    que.append(start)
    check[start] = True

    while que:
        v = que.popleft()
        for i in invite[v]:
            if check[i-1] == False:
                que.append(i-1)
                check[i-1] = True

    else:
        return

bfs(invite, 0, check)

cnt = 0
for j in check[1:]:
    if j == True:
        cnt += 1

print(N - cnt)