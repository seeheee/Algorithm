# 가장 중요했던 부분.... 대각선까지 고려하려면 3차원 배열로 담아야한다.
# 그거를 제외한 아이디어는 맞았는데 메모리제이션인거 헷갈려서 구현 못함
N = int(input())
array = list(list(map(int, input().split())) for _ in range(N))

# 가로, 세로, 대각선 이동 각각 초기화 -> 생각못한 부분: 각각 변수로 초기화하지 말고 하나의 배열안에 넣기
visited = [[[0 for i in range(N)] for i in range(N)] for i in range(3)]

# visited[0]은 가로, visited[1]은 세로, visited[2]는 대각선

# # 틀린방법
# f_visited = [[0]*N for _ in range(N)]
# s_visited = [[0]*N for _ in range(N)]
# t_visited = [[0]*N for _ in range(N)]

visited[0][0][1] = 1  # 막대기 끝 부분 1로 표현

# 첫번째 줄은 가로 밖에 안됨(초기화 한거라 볼 수 있음 for 메모리제이션)
for i in range(2, N):
    if array[0][i] == 0:
        visited[0][0][i] = visited[0][0][i-1]

# 다음 두번째 줄부터 시작
for i in range(1, N):
    # 1에 막대기가 있으니까는
    for j in range(2, N):
        # 대각선일 경우 총 3가지(대각선, 세로, 가로)
        if array[i][j] == 0 and array[i-1][j] == 0 and array[i][j-1] == 0: # 3칸이 0이어야지 대각선 방향으로 이동가능
            visited[2][i][j] = visited[1][i-1][j-1] + visited[2][i-1][j-1] + visited[0][i-1][j-1]

        # 세로일 경우 총 2가지(대각선, 세로)
        if array[i][j] == 0:
            visited[1][i][j] = visited[1][i-1][j] + visited[2][i-1][j]

        # 가로일 경우 총 2가지(대각선, 가로)
        # if array[i][j] == 0:
            visited[0][i][j] = visited[0][i][j-1] + visited[2][i][j-1]

# print(visited)

answer = [visited[a][N-1][N-1] for a in range(3)]
print(sum(answer))






# for i in range(1, N+1):
#     for j in range(2, N+1):
#         if array[i][j] == 1:
#             continue
#         else:
#
#             f_visited[i][j] += f_visited[i][j+1]
#             if i < N and j < N:
#                 f_visited[i][j] += f_visited[i+1][j+1]
#
# print(f_visited[N][N])
