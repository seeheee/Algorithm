import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]
distance = {i:float('inf') for i in range(1, V+1)}
visited = [False] * (V+1)

def bfs(v, adj, distance):
    que = deque()
    que.append(v) # (거리,노드) 힙에 집어넣음
    distance[v] = 0  # 처음 시작노드 초기화
    visited[v] = True
    while que:
        # print(que)
        now = que.popleft() # 거리, 노드
        for next, d in adj[now]:
            if distance[next] > distance[now] + d:
                distance[next] = distance[now] + d
                if visited[next] ==  False:
                    que.append(next)
                    visited[next] = True


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

