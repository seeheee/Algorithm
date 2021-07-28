import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]


# 파티끝내고 돌아가는 최단거리 작성
def distra(start):
    distance = {i: float('inf') for i in range(1, N + 1)}
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
                heapq.heappush(que, (distance[now] + d, next))
    return distance

# 단방향 인접 그래프 생성
for _ in range(M):
    n1, n2, d = map(int, input().split())
    adj[n1].append([n2, d])

# 파티에서 돌아오는 길 + 파티로 가는 길
answer = [0] * (N+1)

# 이걸 함수안에서 받아올라고 했음 밖에서 하나씩 함수로 넣어주면 되는 거 였음...
for i in range(1, N+1):
    arr = distra(i)
    answer[i] += arr[X]


# 파티 마치고 집으로 돌아가는 길
arr2 = distra(X)
for i in range(1, N+1):
    answer[i] += arr2[i]

print(max(answer))


