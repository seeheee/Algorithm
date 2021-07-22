from collections import deque, defaultdict
case = int(input())

def bfs(v, visited, real_adj):
    count = 0
    que = deque([[v, count]])
    while que:
        v, count = que.popleft()
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for i in real_adj[v]:
                que.append([i, count])



# for i in range(case):
N = int(input())
tree = list(list(map(int, input().split())) for _ in range(N-1))
n1, n2 = map(int, input().split())

adj = [[] for _ in range(N+1)]
real_adj = [[] for _ in range(N+1)]
visited = [-1] * (N + 1)

for a,b in tree:
    adj[b].append(a)

# 1. 루트 노드를 찾는다.
for i in range(1, len(adj)):
    if len(adj[i]) == 0:
        root = i

for a, b in tree:
    real_adj[a].append(b)

bfs(root, visited, real_adj)

print(visited)

if visited[n1] < visited[n2]:
    print(n1)
if visited[n1] > visited[n2]:
    print(n2)
if visited[n1] == visited[n2]:
    for j in visited:
        if visited[j] == visited[n1] - 1:
            print(j)


