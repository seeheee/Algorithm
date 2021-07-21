from itertools import combinations
from collections import deque
N = int(input())
human = list(map(int, input().split()))
lands = list(list(map(int, input().split())) for _ in range(N))
# visited = [[0] * (N+1)]
list1 = list([] for _ in range(N+1))
result = float('inf')

def bfs(c):
    start = c[0]
    que = deque([start])
    visited = set([start])
    _sum = 0
    while que:
        v = que.popleft()
        _sum += human[v]
        for j in list1[v]:
            if j not in visited and j in c:
                que.append(j)
                visited.add(v)
    return _sum, len(visited)

# 인접리스트 생성
for land in lands:
    for i in range(1, land[0]+1):
        list1[land[0]].append(land[i])

# 조합(선거구를 어떻게 나눌 것인가)
for i in range(1, N//2+1):
    combi = combinations(range(N), i)
    for c in combi:
        sum1, v1 = bfs(c)
        sum2, v2 = bfs([i for i in range(N) if i not in c])
        if v1 + v2 == N:
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)

print(list1)