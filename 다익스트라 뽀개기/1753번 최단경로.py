import sys
input = sys.stdin.readline
from collections import deque
V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]
distance = {i:float('inf') for i in range(1, V+1)}
print(distance)

def bfs(v, adj, distance):
    que = deque([v])
    distance[v] = 0
    while que:
        v = que.popleft()
        for v1, d in adj[v]:
            if distance[v1] > distance[v] + d:
                distance[v1] = distance[v] + d
                que.append(v1)


# 인접리스트 생성
for i in range(E):
    n1, n2, d = map(int, input().split())
    adj[n1].append([n2, d])


bfs(start, adj, distance)

for i in distance.values():
    if i == float('INF'):
        print("INF")
    else:
        print(i)

