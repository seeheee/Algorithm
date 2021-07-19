# 양방향 그래프 구현 방법
for e in edge:
    adj = [[] for _ in range(n + 1)]
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)


# 한 방향으로의 그래프 구현 방법
    # 인접 리스트 구현(딕셔너리로 구현) - 인접 행렬 방법 밖에 몰랐음
    # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    def link_list():
        dic = defaultdict(list)
        for key, ticket in tickets:
            dic[key].append(ticket)
        return dic


# 내 풀이(BFS - 최단거리)
from collections import deque

def bfs(v, visited, adj):
    count = 0
    que = deque()
    que.append([v, count])
    while que:
        print(que)
        v, count = que.popleft()
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for a in adj[v]:
                que.append([a, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1) # 0으로 초기화하면 노드가 1일때 꼬임
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for idx, value in enumerate(visited):
        if max(visited) == value:
            answer += 1
    return answer