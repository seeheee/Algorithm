def solution(m, n, puddles):
    visited = [[0] * (m + 1) for _ in range(n + 1)]

    # 초기화 작업
    visited[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:  # 2차원 배열안에 특정 리스트가 있으면 (m,n) 3행 4열인데 좌표는 (4,3)으로 주어 짐
                visited[i][j] = 0

            # if i > 1 and j > 1 # 1,2 / 2,1 들어갈수없음

            # 조건이 없으면 초기화 값이 사라짐(0)
            else:
                if i > 1:
                    visited[i][j] += visited[i - 1][j]
                if j > 1:
                    visited[i][j] += visited[i][j - 1]

    return visited[n][m] % 1000000007


def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if [i, j] in puddles:
                dp[j][i] = 0
            else:
                if i == 1 and j == 1:
                    dp[j][i] = 1
                else:
                    dp[j][i] = (dp[j - 1][i] + dp[j][i - 1]) % 1000000007

    return dp[n][m]
