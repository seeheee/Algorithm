import heapq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
distance = {i:float('inf') for i in range(N+1)}

def bfs(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for next, d in adj[now]:
            if distance[next] > distance[now] + d:
                distance[next] = distance[now] + d
                heapq.heappush(que, (distance[now]+d, next))



for i in range(M):
    n1, n2, d = map(int, input().split())
    adj[n1].append([n2, d])

start, end = map(int, input().split())

bfs(start)

print(distance[end])