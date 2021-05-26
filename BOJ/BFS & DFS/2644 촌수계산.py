from collections import deque
n = int(input()) # 전체 사람의 수
P1, P2 = map(int, input().split()) # 서로 다른 사람의 수
m = int(input()) # 관계의 개수
people_list = [[] for _ in range(n+1)]
people_visited = [False for _ in range(n+1)]



def bfs(start, finish):
    count = 0
    que = deque([[start, count]])
    while que:
        node = que.popleft()
        start = node[0]
        count = node[1]
        if start == finish:
            return count
        if not people_visited[start]:
            count += 1
            people_visited[start] = True
            for i in people_list[start]:
                if not people_visited[i]:
                    que.append([i, count])
    return -1

for _ in range(m):
    x, y = map(int, input().split())
    people_list[x].append(y)
    people_list[y].append(x)

print("people_list", people_list)
print("people_visited", people_visited)
print(bfs(1, 4))


