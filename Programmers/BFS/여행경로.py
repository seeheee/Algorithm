# 엄청 어려워... 어려워...
from collections import defaultdict

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
visited = [0 for _ in range(len(tickets) + 1)]


def solution(tickets):

    # 인접 리스트 구현 - 인접 행렬 방법 밖에 몰랐음
    def link_list():
        dic = defaultdict(list)
        for key, ticket in tickets:
            dic[key] = ticket
        return dic

    def bfs(t):
        answer = []
        que = deque()
        que.append(t)
        while que:
            start, stopover = que.popleft()

            if start == 'ICN':
                visited[0] = 1
                answer.append(start)

            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    answer.append()


print(solution(tickets))

