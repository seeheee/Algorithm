# 엄청 어려워... 어려워...
from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
visited = [0 for _ in range(len(tickets) + 1)]

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



def solution(tickets):
    for ticket in tickets:
        bfs(ticket)


print(solution(tickets))

