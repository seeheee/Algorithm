from collections import deque
N, K = map(int, input().split())
MAX = 10 ** 5
visited = [0 for _ in range(MAX+1)]

# 보고 푼 풀이
def bfs(start):
    que = deque()
    que.append(start)
    while que:
        start = que.popleft()
        if start == K:
            print(visited[start])
            break
        # 가능한 모든 수들을 깊이 탐색으로 확장하는 것을 생각못함
        for nstart in (start-1, start+1, start*2):
            # 점은 0부터 10**5까지 가능, 방문을 이미 했다면 그 값은 들어가면 안되니까는
            if 0 <= nstart <= MAX and not visited[nstart]:
                visited[nstart] = visited[start] + 1
                que.append(nstart)

bfs(N)

# # 맨 처음 작성한 코드
# def bfs(start, finish):
#     count = 0
#     visited[start] = True
#     que = deque()
#     que.append([start, finish])
#     while que:
#         nstart, nfinish = que.popleft()
#         print(nstart, nfinish)
#         if nstart * 2 < nfinish:
#             visited[nstart*2] = True
#             nstart = nstart * 2
#             if nstart + 1 == nfinish:
#                 nstart = nstart + 1
#             que.append([nstart, nfinish])
#         elif nstart * 2 > nfinish:
#             nstart -= 1
#             visited[nstart] = True
#             que.append([nstart, nfinish])
#         if nstart == nfinish:
#             visited[nstart] = True
#             break
#
#     for i in visited:
#         if i == True:
#             count += 1
#     return count - 1


