def solution(m, n, puddles):
    visited = [[0 for _ in range(m+1)]for _ in range(n+1)]
    # 1,1에서 출발 (0,0)이 아니다
    # 집 출발점
    visited[1][1] = 1

    for i in range(1, n):
        for j in range(1, m):
            for k in puddles:
                if [i, j] == k:
                    visited[i][j] = 0
            else:
                if i > 1:
                    visited[i][j] += visited[i-1][j]
                if j > 1:
                    visited[i][j] += visited[i][j-1]
    return visited[n-1][m-1]





print(solution(4, 3, [[2, 2]]))