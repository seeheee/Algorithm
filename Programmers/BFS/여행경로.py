# 못 품

from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
visited = [0 for _ in range(len(tickets) + 1)]

def bfs(t):
    que = deque()
    que.append(t[0])
    while que:
        airport = que.popleft()
        for i in range(len(visited)):
            if visited[i] == 0:
                visited[i] = 1



def solution(tickets):
    for ticket in tickets:
        bfs(ticket)


print(solution(tickets))

