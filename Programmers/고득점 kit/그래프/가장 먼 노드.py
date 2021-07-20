# # 양방향 그래프 구현 방법
# for e in edge:
#     adj = [[] for _ in range(n + 1)]
#         x = e[0]
#         y = e[1]
#         adj[x].append(y)
#         adj[y].append(x)
#
#
# # 한 방향으로의 그래프 구현 방법
#     # 인접 리스트 구현(딕셔너리로 구현) - 인접 행렬 방법 밖에 몰랐음
#     # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
#     def link_list():
#         dic = defaultdict(list) # value 값의 초기값이 리스트가 됨
#         for key, ticket in tickets:
#             dic[key].append(ticket)
#         return dic


# 최단거리를 찾을 때는 deque 사용
from collections import deque


def bfs(v, visited, link_list):
    # 거리 초기화
    dis = 0
    que = deque()
    que.append([v, dis])
    while que:
        # print(que)
        v, dis = que.popleft()
        if visited[v] == -1:  # 방문을 했으면 이미 지나간 거 지나간거는 그게 최단거리
            visited[v] = dis  # 방문 표시해주고 최단거리 담기
            dis += 1
            for j in link_list[v]:  # 인접리스트를 돌면서
                que.append([j, dis])  # 거리 증가시켜 돌기


def solution(n, edge):
    answer = 0
    # 인접리스트 초기화
    link_list = [[] for _ in range(n + 1)]
    # 거리 테이블 초기화
    visited = [-1] * (n + 1)
    # 양방향 인접리스트 생성
    for a, b in edge:
        link_list[a].append(b)
        link_list[b].append(a)

    bfs(1, visited, link_list)

    # 가장 멀리 떨어진 노드의 개수 세기
    for i in visited:
        if max(visited) == i:
            answer += 1
    return answer