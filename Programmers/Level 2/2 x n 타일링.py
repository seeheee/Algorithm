# 경우의 수가 큰 것이 배열에 담기면서 계산 속도가 느려진다.
# 이를 막기 위해서 배열 하나를 구할때 마다 1000000007을 계산해준다.

def solution(n):
    DP = [0] * (n + 1)

    DP[1] = 1
    DP[2] = 2

    for i in range(3, n + 1):
        DP[i] = (DP[i - 1] + DP[i - 2]) % 1000000007

    return DP[n]


# # 정확성 전부 통과 효율성에서 시간 초과
# def solution(n):
#     DP = [0] * (n + 1)
#
#     DP[1] = 1
#     DP[2] = 2
#
#     for i in range(3, n + 1):
#         DP[i] = DP[i - 1] + DP[i - 2]
#
#     return DP[n] % 1000000007




