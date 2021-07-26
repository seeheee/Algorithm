import heapq

def solution(N, road, K):
    answer = 0
    adj = [[] for _ in range(N + 1)]
    distance = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    def distra(start):
        que = []
        heapq.heappush(que, (0, start))
        while que:
            dist, now = heapq.heappop(que)
            if distance[now] < dist:
                continue
            for next, d in adj[now]:
                if distance[next] > distance[now] + d:
                    distance[next] = distance[now] + d
                    heapq.heappush(que, (distance[now] + d, next))

    for n1, n2, d in road:
        adj[n1].append([n2, d])
        adj[n2].append([n1, d])

    distra(1)

    for i in distance.values():
        if i <= K:
            answer += 1
    return answer