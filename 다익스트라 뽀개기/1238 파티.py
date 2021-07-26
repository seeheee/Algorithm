import heapq
N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
back_distance = {i:float('inf') for i in range(1, N+1)}
come_distance = {i:float('inf') for i in range(1, N+1)}

# 각각 노드에서 파티하는 곳으로 가는 최단거리 작성
def come(end):
    que = []
    for i in range(1, N+1):
        if i != end:
            heapq.heappush(que, (0, i))
            come_distance[i] = 0
    while que:
        dist, now = heapq.heappop(que)
        if come_distance[now] < dist:
            continue
        for next, d in adj[now]:
            if come_distance[next] > come_distance[now] + d:
                come_distance[next] = come_distance[now] + d
                heapq.heappush(que, (come_distance[now] + d, next))


# 파티끝내고 돌아가는 최단거리 작성
def back(start):
    que = []
    heapq.heappush(que, (0, start))
    back_distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if back_distance[now] < dist:
            continue
        for next, d in adj[now]:
            if back_distance[next] > back_distance[now] + d:
                back_distance[next] = back_distance[now] + d
                heapq.heappush(que, (back_distance[now] + d, next))

# 단방향 인접 그래프 생성
for _ in range(M):
    n1, n2, d = map(int, input().split())
    adj[n1].append([n2, d])

back(X)

come(X)

