def solution(dirs):
    visited = set()
    dic = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    x, y = 0, 0
    answer = 0
    for d in dirs:
        nx = dic[d][0] + x
        ny = dic[d][1] + y
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))  # 양방향이라서 왔던 길이니까는 방문 표시해준다
                answer += 1
            x, y = nx, ny
    return answer

print(solution("LULLLLLLUD"))



from collections import deque
# def solution(dirs):
#     visited = [[0] * 10 for _ in range(10)]
#     count = 0
#     que = deque([[0, 0]])
#     while que:
#         x, y = que.popleft()
#         visited[x][y] = 1
#         for d in dirs:
#             if d == 'U':
#                 nx = x - 1
#                 ny = y
#             elif d == 'D':
#                 nx = x + 1
#                 ny = y
#             elif d == 'R':
#                 nx = x
#                 ny = y + 1
#             elif d == 'L':
#                 nx = x
#                 ny = y - 1
#                 if -5 <= nx <= 5 and -5 <= ny <= 5:
#                     if visited[nx][ny] == 0:
#                         count += 1
#                         visited[nx][ny] = 1
#                 x, y = nx, ny
#
#     print(visited)
#     print(count)